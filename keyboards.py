from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_exit_menu(current_page: str):
    """Универсальное меню выхода для конечных страниц"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')],
        [InlineKeyboardButton(text='⏪ Назад', callback_data=f'back:{current_page}')]
    ])



# === Главное меню ===
main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Образование 📖', callback_data='edu')],
    [InlineKeyboardButton(text='Здоровье 🏥', callback_data='health')],
    [InlineKeyboardButton(text='Стипендия 💰', callback_data='finance')],
    [InlineKeyboardButton(text='Документы 📄', callback_data='documents')],
    [InlineKeyboardButton(text='Общежитие 🏠', callback_data='dormitory')],
    [InlineKeyboardButton(text='Помощь 🆘', callback_data='help')],
    [InlineKeyboardButton(text='Афиша 🎭', callback_data='events')]
])

exit_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
])

# === Образование ===
edu_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1 курс', callback_data='edu_course1')],
    [InlineKeyboardButton(text='2 курс', callback_data='edu_course2')],
    [InlineKeyboardButton(text='Единое окно', callback_data='edu_singlewindow')],
    [InlineKeyboardButton(text='Учебная часть', callback_data='edu_part')],
    [InlineKeyboardButton(text='Электронный университет', callback_data='edu_eluniver')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
])

course_1_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Деятельностные практики', callback_data='edu_course1_practices')],
    [InlineKeyboardButton(text='Английский язык', callback_data='edu_course1_english')],
    [InlineKeyboardButton(text='ЭДФК (пометка, что ТО не отвечает за это)', callback_data='edu_course1_edfk')],
    [InlineKeyboardButton(text='⏪ Назад', callback_data='back:edu_menu')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
])

course_2_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='МООК', callback_data='edu_course2_mooc')],
    [InlineKeyboardButton(text='ДПО', callback_data='edu_course2_dpo')],
    [InlineKeyboardButton(text='Деятельностные практики', callback_data='edu_course2_activity')],
    [InlineKeyboardButton(text='Проектная деятельность', callback_data='edu_course2_project')],
    [InlineKeyboardButton(text='ЭДФК (пометка, что ТО не отвечает за это)', callback_data='edu_course2_edfk')],
    [InlineKeyboardButton(text='Рабочие профессии', callback_data='edu_course2_professions')],
    [InlineKeyboardButton(text='Дисциплины по выбору (что такое / списки / переводы)', callback_data='edu_course2_choices')],
    [InlineKeyboardButton(text='⏪ Назад', callback_data='back:edu_menu')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
])

eluniver_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='eluniver', callback_data='edu_eluniver_eluniver')],
    [InlineKeyboardButton(text='Elios', callback_data='edu_eluniver_elios')],
    [InlineKeyboardButton(text='Справочник', callback_data='edu_eluniver_guide')],
    [InlineKeyboardButton(text='Учебный план', callback_data='edu_eluniver_plan')],
    [InlineKeyboardButton(text='Расписание', callback_data='edu_eluniver_schedule')],
    [InlineKeyboardButton(text='⏪ Назад', callback_data='back:edu_menu')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
])

# === Здоровье ===
health_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Прививки', callback_data='health_vaccinations')],
    [InlineKeyboardButton(text='Справки', callback_data='health_certificates')],
    [InlineKeyboardButton(text='Окб / Профпаталогия', callback_data='health_okb')],
    [InlineKeyboardButton(text='Заболел, куда обратиться?', callback_data='health_sick')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
])

# === Стипендии ===
finance_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Виды стипендий', callback_data='finance_types')],
    [InlineKeyboardButton(text='Матпомощь', callback_data='finance_help')],
    [InlineKeyboardButton(text='Кабинеты', callback_data='finance_cabinets')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
])

# === Документы ===
documents_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Перечень обязательных справок', callback_data='documents_required')],
    [InlineKeyboardButton(text='Военкомат', callback_data='documents_military')],
    [InlineKeyboardButton(text='Временная регистрация', callback_data='documents_registration')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
])

# === Общежитие ===
dormitory_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Как оплатить', callback_data='dormitory_pay')],
    [InlineKeyboardButton(text='Стоимость', callback_data='dormitory_cost')],
    [InlineKeyboardButton(text='Документы', callback_data='dormitory_documents')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
])

# === Помощь ===
help_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Потеряшки', callback_data='help_lost')],
    [InlineKeyboardButton(text='Связь с тьютором', callback_data='help_tutor')],
    [InlineKeyboardButton(text='Тьюториалы (гайды)', callback_data='help_tutorials')],
    [InlineKeyboardButton(text='Частые вопросы', callback_data='help_faq')],
    [InlineKeyboardButton(text='Поддержка', callback_data='help_support')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
])

# === Афиша ===
events_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ноябрь - 5 полей ценностей', callback_data='events_november')],
    [InlineKeyboardButton(text='Декабрь...', callback_data='events_december')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
])


KEYBOARDS = {
    'main_menu': main_menu,
    'edu': edu_menu,
    'edu_course1': course_1_menu,
    'edu_course2': course_2_menu,
    'edu_eluniver': eluniver_menu,
    'health': health_menu,
    'finance': finance_menu,
    'documents': documents_menu,
    'dormitory': dormitory_menu,
    'help': help_menu,
    'events': events_menu,
}