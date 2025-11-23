from aiogram import F, Router
from aiogram.types import CallbackQuery

import keyboards as kb
from utils import get_menu_text, safe_edit_message

router_dormitory = Router()


@router_dormitory.callback_query(F.data == 'dormitory')
async def open_dormitory_menu(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await safe_edit_message(callback.message, text, reply_markup=kb.dormitory_menu)


@router_dormitory.callback_query(F.data == 'dormitory_pay')
async def pay_info(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await safe_edit_message(callback.message, text, reply_markup=kb.get_exit_menu(callback.data))


@router_dormitory.callback_query(F.data == 'dormitory_cost')
async def cost_info(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await safe_edit_message(callback.message, text, reply_markup=kb.get_exit_menu(callback.data))


@router_dormitory.callback_query(F.data == 'dormitory_documents')
async def documents_info(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await safe_edit_message(callback.message, text, reply_markup=kb.get_exit_menu(callback.data))
