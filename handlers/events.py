from aiogram import F, Router
from aiogram.types import CallbackQuery

import keyboards as kb

router_events = Router()


@router_events.callback_query(F.data == 'events')
async def open_events_menu(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('events_menu', reply_markup=kb.events_menu)


@router_events.callback_query(F.data == 'events_november')
async def november(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Вы выбрали {callback.data}', reply_markup=kb.exit_menu)


@router_events.callback_query(F.data == 'events_december')
async def december(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Вы выбрали {callback.data}', reply_markup=kb.exit_menu)
