from aiogram import F, Router
from aiogram.types import CallbackQuery

import keyboards as kb
from utils import get_menu_text

router_help = Router()


@router_help.callback_query(F.data == 'help')
async def open_help_menu(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.help_menu)


@router_help.callback_query(F.data == 'help_lost')
async def lost(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_help.callback_query(F.data == 'help_tutor')
async def tutor(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_help.callback_query(F.data == 'help_tutorials')
async def tutorials(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_help.callback_query(F.data == 'help_faq')
async def faq(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_help.callback_query(F.data == 'help_support')
async def support(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))
