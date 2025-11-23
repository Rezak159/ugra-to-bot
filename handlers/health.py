from aiogram import F, Router
from aiogram.types import CallbackQuery

import keyboards as kb
from utils import get_menu_text, safe_edit_message

router_health = Router()


@router_health.callback_query(F.data == 'health')
async def catalog(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await safe_edit_message(callback.message, text, reply_markup=kb.health_menu)


@router_health.callback_query(F.data == 'health_vaccinations')
async def vaccinations(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await safe_edit_message(callback.message, text, reply_markup=kb.get_exit_menu(callback.data))


@router_health.callback_query(F.data == 'health_certificates')
async def certificates(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await safe_edit_message(callback.message, text, reply_markup=kb.get_exit_menu(callback.data))


@router_health.callback_query(F.data == 'health_okb')
async def okb(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await safe_edit_message(callback.message, text, reply_markup=kb.get_exit_menu(callback.data))


@router_health.callback_query(F.data == 'health_sick')
async def sick(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await safe_edit_message(callback.message, text, reply_markup=kb.get_exit_menu(callback.data))
