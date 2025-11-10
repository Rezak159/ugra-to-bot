from aiogram import F, Router
from aiogram.types import CallbackQuery


import keyboards as kb

router_health = Router()


@router_health.callback_query(F.data == 'health')
async def catalog(callback: CallbackQuery):
    await callback.message.edit_text('health_menu', reply_markup=kb.health_menu)