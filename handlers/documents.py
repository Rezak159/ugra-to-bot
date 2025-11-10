from aiogram import F, Router
from aiogram.types import CallbackQuery

import keyboards as kb

router_documents = Router()


@router_documents.callback_query(F.data == 'documents')
async def open_documents_menu(callback: CallbackQuery):
    await callback.message.edit_text('documents_menu', reply_markup=kb.documents_menu)


