import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram import F

from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import keyboards as kb

from handlers.edu import router_edu
from handlers.health import router_health
from handlers.finance import router_finance
from handlers.documents import router_documents
from handlers.dormitory import router_dormitory
from handlers.help import router_help
from handlers.events import router_events


from config import TG_TOKEN
bot = Bot(token=TG_TOKEN)
dp = Dispatcher()

import datetime

from utils import get_weather

def main_menu_text(first_name):
    current_time = datetime.datetime.now()
    hour = current_time.hour
    
    # Определяем приветствие
    if 0 <= hour < 4:
        text = '🌃 Доброй ночи'
    elif 4 <= hour < 12:
        text = '🌄 Доброе утро'
    elif 12 <= hour < 18:
        text = '☀️ Добрый день'
    else:  # 18 <= hour < 24
        text = '🌇 Добрый вечер'

    # Получаем погоду
    weather = get_weather()
    temp_text = f"{weather['temp']} ❄️" if weather else "0 ❄️"

    return (f'{text}, {first_name}, ты в главном меню\n'
            f'Сейчас на улице: {temp_text}\n')


@dp.message(CommandStart())
async def cmd_start(message: Message):
    text = main_menu_text(message.from_user.first_name)
    await message.answer(text,
                        reply_markup=kb.main_menu)


@dp.callback_query(F.data == 'main_menu')
async def catalog(callback: CallbackQuery):
    text = main_menu_text(callback.from_user.first_name)
    await callback.answer()
    await callback.message.edit_text(text,
                                     reply_markup=kb.main_menu)
    
def get_parent_callback(current):
    """Возвращает родительский callback на основе текущего"""
    root_sections = {'edu', 'health', 'finance', 'documents', 'dormitory', 'help', 'events'}
    
    if current in root_sections:
        return 'main_menu'

    if '_' in current:
        return current.rsplit('_', 1)[0]
    
    return 'main_menu'
    
from utils import get_menu_text
@dp.callback_query(F.data.startswith('back:'))
async def go_back(callback: CallbackQuery):
    await callback.answer()
    
    # Извлекаем текущую позицию из callback
    _, current = callback.data.split(':', 1)
    
    # Вычисляем родительское меню
    parent = get_parent_callback(current)
    
    # Получаем клавиатуру и текст из JSON
    keyboard = kb.KEYBOARDS.get(parent, kb.main_menu)
    text = get_menu_text(parent, callback.from_user.first_name)
    
    await callback.message.edit_text(text, reply_markup=keyboard)


@dp.message(F.text)
async def echo(message: Message):
    await message.reply("🦄 Используй кнопки под сообщениями.\n"
                        "Если потерялся, используй /start")

async def main():
    dp.include_router(router_edu)
    dp.include_router(router_health)
    dp.include_router(router_finance)
    dp.include_router(router_documents)
    dp.include_router(router_dormitory)
    dp.include_router(router_help)
    dp.include_router(router_events)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        print('Успешный запуск.')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')



    