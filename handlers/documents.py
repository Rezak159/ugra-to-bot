from aiogram import F, Router
from aiogram.types import CallbackQuery

import keyboards as kb

router_documents = Router()


@router_documents.callback_query(F.data == 'documents')
async def open_documents_menu(callback: CallbackQuery):
    await callback.message.edit_text('documents_menu', reply_markup=kb.documents_menu)


@router_documents.callback_query(F.data == 'documents_required')
async def required(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Вы выбрали {callback.data}', reply_markup=kb.exit_menu)


@router_documents.callback_query(F.data == 'documents_military')
async def military(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Вы выбрали {callback.data}', reply_markup=kb.exit_menu)


@router_documents.callback_query(F.data == 'documents_registration')
async def registration(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Вы выбрали {callback.data}', reply_markup=kb.exit_menu)
