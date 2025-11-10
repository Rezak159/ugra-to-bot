from aiogram import F, Router
from aiogram.types import CallbackQuery

import keyboards as kb
from utils import get_menu_text

router_edu = Router()


@router_edu.callback_query(F.data.in_({'edu', 'edu_menu'}))
async def open_edu_menu(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text('edu')
    await callback.message.edit_text(text, reply_markup=kb.edu_menu)


@router_edu.callback_query(F.data == 'edu_course1')
async def open_course_1(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.course_1_menu)


@router_edu.callback_query(F.data == 'edu_course2')
async def open_course_2(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.course_2_menu)


@router_edu.callback_query(F.data == 'edu_eluniver')
async def open_eluniver(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.eluniver_menu)


@router_edu.callback_query(F.data == 'edu_part')
async def open_edu_part(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_edu.callback_query(F.data == 'edu_singlewindow')
async def open_single_window(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_edu.callback_query(F.data == 'edu_course1_practices')
async def course1_practices(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_edu.callback_query(F.data == 'edu_course1_english')
async def course1_english(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_edu.callback_query(F.data == 'edu_course1_edfk')
async def course1_edfk(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_edu.callback_query(F.data == 'edu_course2_mooc')
async def course2_mooc(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_edu.callback_query(F.data == 'edu_course2_dpo')
async def course2_dpo(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_edu.callback_query(F.data == 'edu_course2_activity')
async def course2_activity(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_edu.callback_query(F.data == 'edu_course2_project')
async def course2_project(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_edu.callback_query(F.data == 'edu_course2_edfk')
async def course2_edfk(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_edu.callback_query(F.data == 'edu_course2_professions')
async def course2_professions(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_edu.callback_query(F.data == 'edu_course2_choices')
async def course2_choices(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_edu.callback_query(F.data == 'edu_eluniver_eluniver')
async def eluniver_eluniver(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_edu.callback_query(F.data == 'edu_eluniver_elios')
async def eluniver_elios(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_edu.callback_query(F.data == 'edu_eluniver_guide')
async def eluniver_guide(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_edu.callback_query(F.data == 'edu_eluniver_plan')
async def eluniver_plan(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))


@router_edu.callback_query(F.data == 'edu_eluniver_schedule')
async def eluniver_schedule(callback: CallbackQuery):
    await callback.answer()
    text = get_menu_text(callback.data)
    await callback.message.edit_text(text, reply_markup=kb.get_exit_menu(callback.data))
