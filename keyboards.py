from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Обрезание ✂️', callback_data='edu')],
    [InlineKeyboardButton(text='Здоровье 🏥', callback_data='health')],
    [InlineKeyboardButton(text='Стипендия 💰', callback_data='finance')],
    [InlineKeyboardButton(text='Доки 📄', callback_data='documents')],
    [InlineKeyboardButton(text='Общаг 🏠', callback_data='dormitory')],
    [InlineKeyboardButton(text='Помощь 🆘', callback_data='help')],
    [InlineKeyboardButton(text='Афиша 🎭', callback_data='events')]
    ]
)

edu_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1 курс', callback_data='edu2')],
    [InlineKeyboardButton(text='2 курс', callback_data='edu2')],
    [InlineKeyboardButton(text='Единое окно', callback_data='edu2')],
    [InlineKeyboardButton(text='Учебная часть', callback_data='edu2')],
    [InlineKeyboardButton(text='Электронный университет', callback_data='edu2')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
    ]
)

health_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Прививки', callback_data='health2')],
    [InlineKeyboardButton(text='Справки', callback_data='health2')],
    [InlineKeyboardButton(text='Окб / Профпаталогия', callback_data='health2')],
    [InlineKeyboardButton(text='Заболел, куда обратиться?', callback_data='health2')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')]
    ]
)