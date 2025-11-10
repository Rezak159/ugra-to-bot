from aiogram import F, Router
from aiogram.types import CallbackQuery

import keyboards as kb

router_help = Router()


@router_help.callback_query(F.data == 'help')
async def open_help_menu(callback: CallbackQuery):
    await callback.message.edit_text('help_menu', reply_markup=kb.help_menu)


