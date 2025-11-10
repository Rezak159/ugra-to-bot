from aiogram import F, Router
from aiogram.types import CallbackQuery

import keyboards as kb

router_dormitory = Router()


@router_dormitory.callback_query(F.data == 'dormitory')
async def open_dormitory_menu(callback: CallbackQuery):
    await callback.message.edit_text('dormitory_menu', reply_markup=kb.dormitory_menu)


@router_dormitory.callback_query(F.data == 'dormitory_pay')
async def pay_info(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Вы выбрали dormitory_pay', reply_markup=kb.exit_menu)


@router_dormitory.callback_query(F.data == 'dormitory_cost')
async def cost_info(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Вы выбрали dormitory_cost', reply_markup=kb.exit_menu)


@router_dormitory.callback_query(F.data == 'dormitory_documents')
async def documents_info(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Вы выбрали dormitory_documents', reply_markup=kb.exit_menu)
