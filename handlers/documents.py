from aiogram import F, Router
from aiogram.types import CallbackQuery

import keyboards as kb
from utils import get_menu_text, safe_edit_message

from middleware import Middleware
router_documents = Router()
router_documents.callback_query.middleware(Middleware())


@router_documents.callback_query(F.data == 'documents')
async def open_documents_menu(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await safe_edit_message(callback.message, text, reply_markup=kb.documents_menu)


@router_documents.callback_query(F.data == 'documents_required')
async def required(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await safe_edit_message(callback.message, text, reply_markup=kb.get_exit_menu(callback.data))


@router_documents.callback_query(F.data == 'documents_military')
async def military(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await safe_edit_message(callback.message, text, reply_markup=kb.get_exit_menu(callback.data))


@router_documents.callback_query(F.data == 'documents_registration')
async def registration(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await safe_edit_message(callback.message, text, reply_markup=kb.get_exit_menu(callback.data))

