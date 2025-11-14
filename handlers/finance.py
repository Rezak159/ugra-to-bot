from aiogram import F, Router
from aiogram.types import CallbackQuery, FSInputFile

import keyboards as kb
from utils import get_menu_text

router_finance = Router()


@router_finance.callback_query(F.data == 'finance')
async def open_finance_menu(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.finance_menu)


@router_finance.callback_query(F.data == 'finance_types')
async def types(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_finance.callback_query(F.data == 'finance_help')
async def help_info(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))

    doc = FSInputFile("files/Материальная помощь.pdf")
    await callback.message.answer_document(
        document=doc,
        caption="<b>Полное положение о материальной поддержке.</b>"
    )


@router_finance.callback_query(F.data == 'finance_cabinets')
async def cabinets(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))
