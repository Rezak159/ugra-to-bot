import asyncio
import logging
import os
from logging.handlers import RotatingFileHandler
from zoneinfo import ZoneInfo

from aiogram import Bot, Dispatcher
from aiogram import F

from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, BotCommand, BotCommandScopeDefault
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import keyboards as kb
import dbtools

from handlers.edu import router_edu
from handlers.health import router_health
from handlers.finance import router_finance
from handlers.documents import router_documents
from handlers.dormitory import router_dormitory
from handlers.help import router_help

from utils import main_menu_text, get_menu_text, safe_edit_message
import stats

from config import TG_TOKEN

# Настройка логирования
EKB_TZ = ZoneInfo("Asia/Yekaterinburg")
LOGS_DIR = "logs"
BOT_LOG_FILE = os.path.join(LOGS_DIR, "bot.log")

# Создаем папку для логов, если её нет
os.makedirs(LOGS_DIR, exist_ok=True)

# Настраиваем формат логов
log_format = logging.Formatter(
    '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Создаем обработчик для файла с ротацией (макс. 10 МБ, 5 файлов)
file_handler = RotatingFileHandler(
    BOT_LOG_FILE,
    maxBytes=10 * 1024 * 1024,  # 10 МБ
    backupCount=5,
    encoding='utf-8'
)
file_handler.setLevel(logging.ERROR)  # Только ошибки и критические
file_handler.setFormatter(log_format)

# Создаем обработчик для консоли
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(log_format)

# Настраиваем корневой логгер
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Настраиваем логгер для aiogram
aiogram_logger = logging.getLogger('aiogram')
aiogram_logger.setLevel(logging.WARNING)  # Только предупреждения и ошибки

bot = Bot(
    token=TG_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


ERROR_TEXT = "😔 Что-то пошло не так. Попробуйте позже."


async def handle_interaction_error(event, exc: Exception):
    """Обработка ошибок взаимодействия с ботом"""
    # Получаем информацию о пользователе и событии
    user_id = None
    username = "Unknown"
    event_type = "Unknown"
    
    if isinstance(event, CallbackQuery):
        user_id = event.from_user.id if event.from_user else None
        username = (event.from_user.username or event.from_user.first_name or "Unknown") if event.from_user else "Unknown"
        event_type = f"CallbackQuery: {event.data if hasattr(event, 'data') else 'unknown'}"
    elif isinstance(event, Message):
        user_id = event.from_user.id if event.from_user else None
        username = (event.from_user.username or event.from_user.first_name or "Unknown") if event.from_user else "Unknown"
        event_type = f"Message: {event.text[:50] if event.text else 'no text'}"
    
    # Логируем ошибку с контекстом
    logger.error(
        f"Ошибка при обработке события | "
        f"Пользователь: {username} (ID: {user_id}) | "
        f"Тип события: {event_type} | "
        f"Ошибка: {type(exc).__name__}: {str(exc)}",
        exc_info=exc
    )
    
    # Отправляем сообщение пользователю
    if isinstance(event, CallbackQuery):
        try:
            await event.answer(ERROR_TEXT, show_alert=True)
        except Exception:
            pass
        try:
            if event.message:
                await event.message.answer(ERROR_TEXT)
        except Exception:
            pass
    elif isinstance(event, Message):
        try:
            await event.answer(ERROR_TEXT)
        except Exception:
            pass

from middleware import check_user_in_group

@dp.message(CommandStart())
async def cmd_start(message: Message):
    try:
        if message.chat.type != 'private':
            return

        username = message.from_user.username or message.from_user.first_name or "Unknown"
        # Проверка на членство
        is_member = await check_user_in_group(bot, message.from_user.id, username)

        if not is_member:
            await message.answer("❌ У вас нет доступа")
            return
        
        # Добавляем пользователя в БД
        dbtools.add_user(message.from_user.id, username)
        dbtools.update_last_request(message.from_user.id)
        stats.log_request(message.from_user.id, username, "command:/start")
        
        text = main_menu_text(message.from_user.first_name)
        await message.answer(text, reply_markup=kb.main_menu)
    except Exception as exc:
        await handle_interaction_error(message, exc)



@dp.callback_query(F.data == 'main_menu')
async def catalog(callback: CallbackQuery):
    try:
        if not callback.message or callback.message.chat.type != 'private':
            await callback.answer('Бот доступен только в личных сообщениях', show_alert=True)
            return

        text = main_menu_text(callback.from_user.first_name)
        await callback.answer()
        await safe_edit_message(callback.message, text, reply_markup=kb.main_menu)
    except Exception as exc:
        await handle_interaction_error(callback, exc)
    
def get_parent_callback(current):
    """Возвращает родительский callback на основе текущего"""
    root_sections = {'edu', 'health', 'finance', 'documents', 'dormitory', 'help'}
    
    if current in root_sections:
        return 'main_menu'

    if '_' in current:
        return current.rsplit('_', 1)[0]
    
    return 'main_menu'
    
@dp.callback_query(F.data.startswith('back:'))
async def go_back(callback: CallbackQuery):
    try:
        if not callback.message or callback.message.chat.type != 'private':
            await callback.answer('Бот доступен только в личных сообщениях', show_alert=True)
            return

        await callback.answer()
        
        # Извлекаем текущую позицию из callback
        _, current = callback.data.split(':', 1)
        
        # Вычисляем родительское меню
        parent = get_parent_callback(current)
        
        # Получаем клавиатуру и текст из JSON
        keyboard = kb.KEYBOARDS.get(parent, kb.main_menu)
        text = get_menu_text(parent, callback.from_user.first_name)

        await safe_edit_message(callback.message, text, reply_markup=keyboard)
    except Exception as exc:
        await handle_interaction_error(callback, exc)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRequestChat
from aiogram.filters import Command

@dp.message(Command("check"))
async def cmd_check(message: Message):
    # Создаем кнопку запроса чата
    # request_id - любой уникальный ID запроса, чтобы различать кнопки
    btn_request = KeyboardButton(
        text="📢 Выбрать группу", 
        request_chat=KeyboardButtonRequestChat(
            request_id=1488,
            request_title=True,
            chat_is_channel=False,
            chat_is_forum=False
        )
    )
    
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[btn_request]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    dbtools.update_last_request(message.from_user.id)
    stats.log_request(message.from_user.id, message.from_user.username or "Unknown", "command:/check")

    await message.answer(
        "Нажмите кнопку ниже, чтобы выбрать группу и узнать её ID:", 
        reply_markup=keyboard
    )

#  Ловит результат выбора (ID группы)
@dp.message(F.chat_shared)
async def on_chat_shared(message: Message):
    chat_id = message.chat_shared.chat_id
    chat_title = message.chat_shared.title
    dbtools.update_last_request(message.from_user.id)
    stats.log_request(message.from_user.id, message.from_user.username or "Unknown", "chat_shared")
    
    await message.answer(
        f"✅ Вы выбрали группу: <b>{chat_title}</b>\n"
        f"🆔 ID группы: <code>{chat_id}</code>"
    )


@dp.message(F.text)
async def echo(message: Message):
    try:
        if message.chat.type != 'private':
            return

        dbtools.update_last_request(message.from_user.id)
        stats.log_request(message.from_user.id, message.from_user.username or "Unknown", "text:unknown")

        await message.reply("🦄 Используй кнопки под сообщениями.\n"
                            "Если потерялся, используй /start")
    except Exception as exc:
        await handle_interaction_error(message, exc)
    

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Открыть меню')
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def errors_handler(event, exception):
    """Глобальный обработчик ошибок aiogram"""
    try:
        user_id = None
        username = "Unknown"
        event_type = "Unknown"
        
        # Определяем тип события и извлекаем информацию о пользователе
        if isinstance(event, Message):
            user_id = event.from_user.id if event.from_user else None
            username = (event.from_user.username or event.from_user.first_name or "Unknown") if event.from_user else "Unknown"
            event_type = f"Message: {event.text[:50] if event.text else 'no text'}"
        elif isinstance(event, CallbackQuery):
            user_id = event.from_user.id if event.from_user else None
            username = (event.from_user.username or event.from_user.first_name or "Unknown") if event.from_user else "Unknown"
            event_type = f"CallbackQuery: {event.data if hasattr(event, 'data') else 'unknown'}"
        elif hasattr(event, 'update') and event.update:
            # Если это объект Update
            update = event.update
            if update.message:
                user_id = update.message.from_user.id if update.message.from_user else None
                username = (update.message.from_user.username or update.message.from_user.first_name or "Unknown") if update.message.from_user else "Unknown"
                event_type = "Update.Message"
            elif update.callback_query:
                user_id = update.callback_query.from_user.id if update.callback_query.from_user else None
                username = (update.callback_query.from_user.username or update.callback_query.from_user.first_name or "Unknown") if update.callback_query.from_user else "Unknown"
                event_type = "Update.CallbackQuery"
        
        logger.error(
            f"Необработанная ошибка aiogram | "
            f"Пользователь: {username} (ID: {user_id}) | "
            f"Тип события: {event_type} | "
            f"Тип ошибки: {type(exception).__name__} | "
            f"Ошибка: {str(exception)}",
            exc_info=exception
        )
    except Exception as log_exc:
        logger.error(f"Ошибка при логировании ошибки: {log_exc}", exc_info=log_exc)
    
    return True  # Возвращаем True, чтобы aiogram не логировал ошибку повторно

async def main():
    dp.include_router(router_edu)
    dp.include_router(router_health)
    dp.include_router(router_finance)
    dp.include_router(router_documents)
    dp.include_router(router_dormitory)
    dp.include_router(router_help)
    
    # Регистрируем глобальный обработчик ошибок
    dp.errors.register(errors_handler)

    await set_commands(bot)
    logger.info("Бот успешно запущен")
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        logger.info("Запуск бота...")
        print('Успешный запуск.')
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Остановка бота по запросу пользователя")
        print('Exit')
    except Exception as exc:
        logger.critical(f"Критическая ошибка при запуске бота: {exc}", exc_info=exc)
        raise



    
