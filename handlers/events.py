from aiogram import F, Router
from aiogram.types import CallbackQuery

import keyboards as kb

router_events = Router()


@router_events.callback_query(F.data == 'events')
async def open_events_menu(callback: CallbackQuery):
    await callback.message.edit_text('events_menu', reply_markup=kb.events_menu)


