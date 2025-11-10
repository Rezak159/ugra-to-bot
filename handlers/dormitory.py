from aiogram import F, Router
from aiogram.types import CallbackQuery

import keyboards as kb

router_dormitory = Router()


@router_dormitory.callback_query(F.data == 'dormitory')
async def open_dormitory_menu(callback: CallbackQuery):
    await callback.message.edit_text('dormitory_menu', reply_markup=kb.dormitory_menu)


