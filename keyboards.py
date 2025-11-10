from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Образование 📖', callback_data='edu')],
    [InlineKeyboardButton(text='Здоровье 🏥', callback_data='health')],
    [InlineKeyboardButton(text='Стипендия 💰', callback_data='finance')],
    [InlineKeyboardButton(text='Документы 📄', callback_data='documents')],
    [InlineKeyboardButton(text='Общежитие 🏠', callback_data='dormitory')],
    [InlineKeyboardButton(text='Помощь 🆘', callback_data='help')],
    [InlineKeyboardButton(text='Афиша 🎭', callback_data='events')]
    ]
)

edu_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1 курс', callback_data='course_1')],
    [InlineKeyboardButton(text='2 курс', callback_data='course_2')],
    [InlineKeyboardButton(text='Единое окно', callback_data='single_window')],
    [InlineKeyboardButton(text='Учебная часть', callback_data='edu_part')],
    [InlineKeyboardButton(text='Электронный университет', callback_data='eluniver')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
    ]
)

course_1_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Деятельностные практики', callback_data='xxx')],
    [InlineKeyboardButton(text='Английский язык', callback_data='xxx')],
    [InlineKeyboardButton(text='ЭДФК (пометка, что ТО не отвечает за это)', callback_data='xxx')],
    [InlineKeyboardButton(text='⏪ Назад', callback_data='edu_menu')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
    ]
)

course_2_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='МООК', callback_data='xxx')],
    [InlineKeyboardButton(text='ДПО', callback_data='xxx')],
    [InlineKeyboardButton(text='Деятельностные практики', callback_data='xxx')],
    [InlineKeyboardButton(text='Проектная деятельность', callback_data='xxx')],
    [InlineKeyboardButton(text='ЭДФК (пометка, что ТО не отвечает за это)', callback_data='xxx')],
    [InlineKeyboardButton(text='Рабочие профессии', callback_data='xxx')],
    [InlineKeyboardButton(text='Дисциплины по выбору (что такое / списки / переводы)', callback_data='xxx')],
    [InlineKeyboardButton(text='⏪ Назад', callback_data='edu_menu')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
    ]
)

eluniver_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='eluniver', callback_data='xxx')],
    [InlineKeyboardButton(text='Elios', callback_data='xxx')],
    [InlineKeyboardButton(text='Справочник', callback_data='xxx')],
    [InlineKeyboardButton(text='Учебный план', callback_data='xxx')],
    [InlineKeyboardButton(text='Расписание', callback_data='xxx')],
    [InlineKeyboardButton(text='⏪ Назад', callback_data='edu_menu')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
    ]
)

# =================================

health_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Прививки', callback_data='health2')],
    [InlineKeyboardButton(text='Справки', callback_data='health2')],
    [InlineKeyboardButton(text='Окб / Профпаталогия', callback_data='health2')],
    [InlineKeyboardButton(text='Заболел, куда обратиться?', callback_data='health2')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
    ]
)

finance_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Виды стипендий', callback_data='finance2')],
    [InlineKeyboardButton(text='Матпомощь', callback_data='finance2')],
    [InlineKeyboardButton(text='Кабинеты', callback_data='finance2')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
    ]
)

documents_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Перечень обязательных справок', callback_data='documents2')],
    [InlineKeyboardButton(text='Военкомат', callback_data='documents2')],
    [InlineKeyboardButton(text='Временная регистрация', callback_data='documents2')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
    ]
)

dormitory_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Как оплатить', callback_data='dormitory2')],
    [InlineKeyboardButton(text='Стоимость', callback_data='dormitory2')],
    [InlineKeyboardButton(text='Документы', callback_data='dormitory2')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
    ]
)

help_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Потеряшки', callback_data='help2')],
    [InlineKeyboardButton(text='Связь с тьютором', callback_data='help2')],
    [InlineKeyboardButton(text='Тьюториалы (гайды)', callback_data='help2')],
    [InlineKeyboardButton(text='Частые вопросы', callback_data='help2')],
    [InlineKeyboardButton(text='Поддержка', callback_data='help2')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
    ]
)

events_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ноябрь - 5 полей ценностей', callback_data='events2')],
    [InlineKeyboardButton(text='Декабрь...', callback_data='events2')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
    ]
)