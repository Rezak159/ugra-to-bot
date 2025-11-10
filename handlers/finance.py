from aiogram import F, Router
from aiogram.types import CallbackQuery

import keyboards as kb

router_finance = Router()


@router_finance.callback_query(F.data == 'finance')
async def open_finance_menu(callback: CallbackQuery):
    await callback.message.edit_text('finance_menu', reply_markup=kb.finance_menu)


@router_finance.callback_query(F.data == 'finance_types')
async def types(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Вы выбрали {callback.data}', reply_markup=kb.exit_menu)


@router_finance.callback_query(F.data == 'finance_help')
async def help_info(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Вы выбрали {callback.data}', reply_markup=kb.exit_menu)


@router_finance.callback_query(F.data == 'finance_cabinets')
async def cabinets(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Вы выбрали {callback.data}', reply_markup=kb.exit_menu)
