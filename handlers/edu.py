from aiogram import F, Router
from aiogram.types import CallbackQuery


import keyboards as kb

router_edu = Router()


@router_edu.callback_query(F.data == 'edu')
async def catalog(callback: CallbackQuery):
    await callback.message.edit_text('edu_menu', reply_markup=kb.edu_menu)