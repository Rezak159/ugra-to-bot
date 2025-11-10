from aiogram import F, Router
from aiogram.types import CallbackQuery

import keyboards as kb
from utils import get_menu_text

router_events = Router()


@router_events.callback_query(F.data == 'events')
async def open_events_menu(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.events_menu)


@router_events.callback_query(F.data == 'events_november')
async def november(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_events.callback_query(F.data == 'events_december')
async def december(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))
