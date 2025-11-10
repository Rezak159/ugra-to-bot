from aiogram import F, Router
from aiogram.types import CallbackQuery


import keyboards as kb

router_edu = Router()


@router_edu.callback_query(F.data == 'edu')
async def catalog(callback: CallbackQuery):
    await callback.message.edit_text('edu_menu', reply_markup=kb.edu_menu)


@router_edu.callback_query(F.data == 'course_1')
async def catalog(callback: CallbackQuery):
    await callback.message.edit_text('course_1_menu', reply_markup=kb.course_1_menu)

@router_edu.callback_query(F.data == 'course_2')
async def catalog(callback: CallbackQuery):
    await callback.message.edit_text('course_2_menu', reply_markup=kb.course_2_menu)

@router_edu.callback_query(F.data == 'eluniver')
async def catalog(callback: CallbackQuery):
    await callback.message.edit_text('eluniver_menu', reply_markup=kb.eluniver_menu)

@router_edu.callback_query(F.data == 'edu_part')
async def catalog(callback: CallbackQuery):
    await callback.message.edit_text('edu_part')

@router_edu.callback_query(F.data == 'single_window')
async def catalog(callback: CallbackQuery):
    await callback.message.edit_text('single_window')