from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_exit_menu(current_page: str):
    """Универсальное меню выхода для конечных страниц"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='⏪ Назад', callback_data=f'back:{current_page}')],
        [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
        
    ])



# === Главное меню ===
main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Образование 📖', callback_data='edu')],
    [InlineKeyboardButton(text='Здоровье 🏥', callback_data='health')],
    [InlineKeyboardButton(text='Стипендия и мат-помощь 💰', callback_data='finance')],
    [InlineKeyboardButton(text='Документы 📄', callback_data='documents')],
    [InlineKeyboardButton(text='Общежитие 🏠', callback_data='dormitory')],
    [InlineKeyboardButton(text='Помощь и тьюторы 🆘', callback_data='help')],
    [InlineKeyboardButton(text='Афиша 🎭', url='https://www.google.com')]
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
    [InlineKeyboardButton(text='ЭДФК', callback_data='edu_course1_edfk')],
    [InlineKeyboardButton(text='⏪ Назад', callback_data='back:edu_menu')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
])

course_2_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='МООК', callback_data='edu_course2_mooc')],
    [InlineKeyboardButton(text='ДПО', callback_data='edu_course2_dpo')],
    [InlineKeyboardButton(text='Проектная деятельность', callback_data='edu_course2_project')],
    [InlineKeyboardButton(text='Рабочие профессии', callback_data='edu_course2_professions')],
    [InlineKeyboardButton(text='Дисциплины по выбору', callback_data='edu_course2_choices')],
    [InlineKeyboardButton(text='⏪ Назад', callback_data='back:edu_menu')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
])

eluniver_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⏪ Назад', callback_data='back:edu_menu')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
])

# === Здоровье ===
health_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Прививки', callback_data='health_vaccinations')],
    [InlineKeyboardButton(text='Справки', callback_data='health_certificates')],
    [InlineKeyboardButton(text='Прикрепление к поликлинике', callback_data='health_okb')],
    [InlineKeyboardButton(text='Заболел, куда обратиться?', callback_data='health_sick')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
])

# === Стипендии и мат-помощь ===
finance_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Виды стипендий', callback_data='finance_types')],
    [InlineKeyboardButton(text='Мат-помощь', callback_data='finance_help')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
])

finance_help_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Куда нести заявление?', callback_data='finance_help_cabinet')],
    [InlineKeyboardButton(text='⏪ Назад', callback_data='back:finance_menu')],
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
    [InlineKeyboardButton(text='Кто такой тьютор', callback_data='help_who-is-tutor')],
    [InlineKeyboardButton(text='Связь с тьютором', callback_data='help_tutor')],
    [InlineKeyboardButton(text='Потеряшки', callback_data='help_lost')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
])


KEYBOARDS = {
    'main_menu': main_menu,
    'edu': edu_menu,
    'edu_course1': course_1_menu,
    'edu_course2': course_2_menu,
    'edu_eluniver': eluniver_menu,
    'health': health_menu,
    'finance_help': finance_help_menu,
    'finance': finance_menu,
    'documents': documents_menu,
    'dormitory': dormitory_menu,
    'help': help_menu,
}
