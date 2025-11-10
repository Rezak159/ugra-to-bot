from aiogram import F, Router
from aiogram.types import CallbackQuery

import keyboards as kb

router_finance = Router()


@router_finance.callback_query(F.data == 'finance')
async def open_finance_menu(callback: CallbackQuery):
    await callback.message.edit_text('finance_menu', reply_markup=kb.finance_menu)


