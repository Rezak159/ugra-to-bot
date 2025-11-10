from aiogram import F, Router
from aiogram.types import CallbackQuery

import keyboards as kb

router_health = Router()


@router_health.callback_query(F.data == 'health')
async def catalog(callback: CallbackQuery):
    await callback.message.edit_text('health_menu', reply_markup=kb.health_menu)


@router_health.callback_query(F.data == 'health_vaccinations')
async def vaccinations(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Вы выбрали {callback.data}', reply_markup=kb.exit_menu)


@router_health.callback_query(F.data == 'health_certificates')
async def certificates(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Вы выбрали {callback.data}', reply_markup=kb.exit_menu)


@router_health.callback_query(F.data == 'health_okb')
async def okb(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Вы выбрали {callback.data}', reply_markup=kb.exit_menu)


@router_health.callback_query(F.data == 'health_sick')
async def sick(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Вы выбрали {callback.data}', reply_markup=kb.exit_menu)
