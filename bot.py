import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram import F

from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import keyboards as kb

from handlers.edu import router_edu
from handlers.health import router_health


from config import TG_TOKEN
bot = Bot(token=TG_TOKEN)
dp = Dispatcher()

def get_wheather():
    API_key = 'b635acfaf84ddc68c16ec1764d0290fd'
    lat = '61.000927'
    lon = '69.029889'

    import requests
    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}")

def main_menu_text(first_name):
    return (f'Добрый день, {first_name}, ты в главном меню\n'
            f'Сейчас на улице: -12 ❄️\n')


@dp.message(CommandStart())
async def cmd_start(message: Message):
    text = main_menu_text(message.from_user.first_name)
    await message.answer(text,
                        reply_markup=kb.main_menu)


@dp.callback_query(F.data == 'main_menu')
async def catalog(callback: CallbackQuery):
    text = main_menu_text(callback.from_user.first_name)
    await callback.message.edit_text(text,
                                     reply_markup=kb.main_menu)


@dp.message(F.text)
async def echo(message: Message):
    await message.reply("🦄 Используй кнопки под сообщениями.\n"
                        "Если потерялся используй /start")

async def main():
    dp.include_router(router_edu)
    dp.include_router(router_health)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        print('Успешный запуск.')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')



    