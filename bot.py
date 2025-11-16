import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram import F

from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, BotCommand, BotCommandScopeDefault
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import keyboards as kb

from handlers.edu import router_edu
from handlers.health import router_health
from handlers.finance import router_finance
from handlers.documents import router_documents
from handlers.dormitory import router_dormitory
from handlers.help import router_help
from handlers.events import router_events

from utils import main_menu_text, get_menu_text

from config import TG_TOKEN
bot = Bot(
    token=TG_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


ERROR_TEXT = "😔 Что-то пошло не так. Попробуйте позже."


async def handle_interaction_error(event, exc: Exception):
    logging.exception("Unhandled error during bot interaction", exc_info=exc)
    if isinstance(event, CallbackQuery):
        try:
            await event.answer(ERROR_TEXT, show_alert=True)
        except Exception:
            pass
        try:
            await event.message.answer(ERROR_TEXT)
        except Exception:
            pass
    elif isinstance(event, Message):
        try:
            await event.answer(ERROR_TEXT)
        except Exception:
            pass


@dp.message(CommandStart())
async def cmd_start(message: Message):
    try:
        text = main_menu_text(message.from_user.first_name)
        await message.answer(text, reply_markup=kb.main_menu)
    except Exception as exc:
        await handle_interaction_error(message, exc)


@dp.callback_query(F.data == 'main_menu')
async def catalog(callback: CallbackQuery):
    try:
        text = main_menu_text(callback.from_user.first_name)
        await callback.answer()
        await callback.message.edit_text(text, reply_markup=kb.main_menu)
    except Exception as exc:
        await handle_interaction_error(callback, exc)
    
def get_parent_callback(current):
    """Возвращает родительский callback на основе текущего"""
    root_sections = {'edu', 'health', 'finance', 'documents', 'dormitory', 'help', 'events'}
    
    if current in root_sections:
        return 'main_menu'

    if '_' in current:
        return current.rsplit('_', 1)[0]
    
    return 'main_menu'
    
@dp.callback_query(F.data.startswith('back:'))
async def go_back(callback: CallbackQuery):
    try:
        await callback.answer()
        
        # Извлекаем текущую позицию из callback
        _, current = callback.data.split(':', 1)
        
        # Вычисляем родительское меню
        parent = get_parent_callback(current)
        
        # Получаем клавиатуру и текст из JSON
        keyboard = kb.KEYBOARDS.get(parent, kb.main_menu)
        text = get_menu_text(parent, callback.from_user.first_name)
        
        await callback.message.edit_text(text, reply_markup=keyboard)
    except Exception as exc:
        await handle_interaction_error(message, exc)

@dp.message(F.text)
async def echo(message: Message):
    try:
        await message.reply("🦄 Используй кнопки под сообщениями.\n"
                            "Если потерялся, используй /start")
    except Exception as exc:
        await handle_interaction_error(message, exc)
    

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Открыть меню')
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def main():
    dp.include_router(router_edu)
    dp.include_router(router_health)
    dp.include_router(router_finance)
    dp.include_router(router_documents)
    dp.include_router(router_dormitory)
    dp.include_router(router_help)
    dp.include_router(router_events)

    await set_commands(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        print('Успешный запуск.')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')



    
