import datetime
import json
from datetime import timedelta
from html import escape

import requests
from aiogram.exceptions import TelegramBadRequest


async def safe_edit_message(message, text):
    """Edit message text without crashing on `message is not modified` errors."""
    current_text = getattr(message, "text", None)

    # Skip redundant edits when both text and markup already match the target.
    if current_text == text:
        return

    try:
        await message.edit_text(text)
    except TelegramBadRequest as exc:
        if "message is not modified" in str(exc).lower():
            return
        raise

_weather_cache = {}


def get_weather():
    """Возвращает погоду с простым кэшированием на 1 час."""
    global _weather_cache

    now = datetime.datetime.now()
    last_update = _weather_cache.get('weather_last_update', datetime.datetime(2000, 1, 1))
    if _weather_cache and now - last_update < timedelta(hours=1):
        return _weather_cache

    API_key = 'b635acfaf84ddc68c16ec1764d0290fd'
    lat = '61.000927'
    lon = '69.029889'
    
    # Добавляем units=metric для получения температуры в Цельсиях
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        # Проверяем успешность запроса
        if data.get('cod') == 200:
            _weather_cache = {
                'temp': round(data['main']['temp']),
                'feels_like': round(data['main']['feels_like']),
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'weather_last_update': datetime.datetime.now()
            }
            return _weather_cache
        return None
    except Exception as e:
        print(f"Ошибка при получении погоды: {e}")
        return None


# Глобальная переменная для кэширования текстов
_texts_cache = None


def load_texts():
    """Загружает тексты из JSON файла один раз и кэширует"""
    global _texts_cache

    if _texts_cache is not None:
        return _texts_cache

    try:
        with open('texts.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        _texts_cache = {}
        for key, value in data.items():
            if isinstance(value, list):
                _texts_cache[key] = "".join(value)
            else:
                _texts_cache[key] = value

        print("✅ Тексты загружены из texts.json")
    except FileNotFoundError:
        print("⚠️ Файл texts.json не найден")
        _texts_cache = {}
    except json.JSONDecodeError as e:
        print(f"❌ Ошибка в texts.json: {e}")
        _texts_cache = {}

    return _texts_cache


def get_menu_text(callback_data, user_name=None):
    """
    Получить текст меню по callback_data

    callback_data: ключ меню (например, 'edu', 'edu_course1')
    user_name: имя пользователя для главного меню
    """
    # Специальная обработка главного меню
    if callback_data == 'main_menu':
        if user_name:
            return main_menu_text(user_name)
        texts = load_texts()
        return texts.get('main_menu', 'Главное меню')

    texts = load_texts()
    return texts.get(callback_data, callback_data)


def translate_weather_description(description):
    """Переводит описание погоды на русский"""
    translations = {
        'clear sky': 'ясно',
        'few clouds': 'малооблачно',
        'scattered clouds': 'облачно',
        'broken clouds': 'облачно',
        'overcast clouds': 'пасмурно',
        'light rain': 'небольшой дождь',
        'moderate rain': 'дождь',
        'heavy rain': 'сильный дождь',
        'snow': 'снег',
        'mist': 'туман',
        'thunderstorm': 'гроза'
    }
    return translations.get(description, description)

def get_weather_emoji(description):
    """Подбирает эмодзи в зависимости от типа погоды"""
    description = description.lower()
    
    # Гроза
    if 'thunderstorm' in description or 'гроза' in description:
        return '⛈️'
    
    # Снег
    elif 'snow' in description or 'снег' in description:
        return '🌨️'
    elif 'sleet' in description or 'град' in description:
        return '🌨️'
    
    # Дождь
    elif 'rain' in description or 'дождь' in description:
        if 'light' in description or 'небольшой' in description:
            return '🌦️'
        return '🌧️'
    elif 'drizzle' in description or 'морось' in description:
        return '🌦️'
    
    # Туман, дымка
    elif any(word in description for word in ['mist', 'fog', 'haze', 'туман', 'дымка']):
        return '🌫️'
    
    # Облачность
    elif 'overcast' in description or 'пасмурно' in description:
        return '☁️'
    elif 'clouds' in description or 'облачно' in description:
        if 'few' in description or 'малооблачно' in description:
            return '🌤️'
        elif 'scattered' in description or 'broken' in description:
            return '⛅'
        return '☁️'
    
    # Ясно
    elif 'clear' in description or 'ясно' in description:
        return '☀️'
    
    # По умолчанию
    return '🌡️'

from aiogram.utils.formatting import Text, Bold
def main_menu_text(first_name):
    """Формирует текст главного меню с приветствием и погодой."""
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 0 <= hour < 4:
        greeting = 'Доброй ночи'
    elif 4 <= hour < 12:
        greeting = 'Доброе утро'
    elif 12 <= hour < 18:
        greeting = 'Добрый день'
    else:
        greeting = 'Добрый вечер'

    weather = get_weather()
    if weather:
        temp = weather['temp']
        temp_str = f'+{temp}' if temp > 0 else str(temp)
        description = translate_weather_description(weather['description'])
        emoji = get_weather_emoji(description)
        weather_text = f"На улице: {temp_str} {emoji}\n"
    else:
        weather_text = ''

    # защита от html инъекций
    safe_name = escape(first_name or 'студент')

    content = (
            f'👋 {greeting}, <b>{safe_name}!</b>\n'
            f'{weather_text}'
            f'Ты в главном меню. С чего начнём?\n')

    return content
