from aiogram import F, Router
from aiogram.types import CallbackQuery

import keyboards as kb

router_help = Router()


@router_help.callback_query(F.data == 'help')
async def open_help_menu(callback: CallbackQuery):
    await callback.message.edit_text('help_menu', reply_markup=kb.help_menu)


@router_help.callback_query(F.data == 'help_lost')
async def lost(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Вы выбрали {callback.data}', reply_markup=kb.exit_menu)


@router_help.callback_query(F.data == 'help_tutor')
async def tutor(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Вы выбрали {callback.data}', reply_markup=kb.exit_menu)


@router_help.callback_query(F.data == 'help_tutorials')
async def tutorials(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Вы выбрали {callback.data}', reply_markup=kb.exit_menu)


@router_help.callback_query(F.data == 'help_faq')
async def faq(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Вы выбрали {callback.data}', reply_markup=kb.exit_menu)


@router_help.callback_query(F.data == 'help_support')
async def support(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Вы выбрали {callback.data}', reply_markup=kb.exit_menu)
