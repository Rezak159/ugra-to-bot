import datetime
from datetime import timedelta


_weather_cache = {}


def get_weather():
    import requests

    now = datetime.datetime.now()
    last_update = _weather_cache.get('weather_last_update', datetime.datetime(2000, 1, 1))
    if _weather_cache:
        if now - last_update < timedelta(hours=1):
            return _weather_cache
    
    API_key = 'b635acfaf84ddc68c16ec1764d0290fd'
    lat = '61.000927'
    lon = '69.029889'
    
    # Добавляем units=metric для получения температуры в Цельсиях
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Проверяем успешность запроса
        if data.get('cod') == 200:
            temp = round(data['main']['temp'])  # Температура в °C
            feels_like = round(data['main']['feels_like'])  # Ощущается как
            description = data['weather'][0]['description']  # Описание погоды
            humidity = data['main']['humidity']  # Влажность
            wind_speed = data['wind']['speed']  # Скорость ветра м/с
            
            return {
                'temp': temp,
                'feels_like': feels_like,
                'description': description,
                'humidity': humidity,
                'wind_speed': wind_speed,
                'weather_last_update': datetime.datetime.now()
            }
        else:
            return None
    except Exception as e:
        print(f"Ошибка при получении погоды: {e}")
        return None



# utils.py
import json

# Глобальная переменная для кэширования текстов
_texts_cache = None

def load_texts():
    """Загружает тексты из JSON файла один раз и кэширует"""
    global _texts_cache
    
    # Если уже загружены - возвращаем кэш
    if _texts_cache is not None:
        return _texts_cache
    
    # Загружаем из файла
    try:
        with open('texts.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            # Обрабатываем массивы строк - объединяем их
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
            return main_menu_text(user_name)  # твоя функция с приветствием
        else:
            texts = load_texts()
            return texts.get('main_menu', 'Главное меню')
    
    # Для остальных - из JSON
    texts = load_texts()
    return texts.get(callback_data, callback_data)  # если нет в JSON - вернём сам callback

def reload_texts():
    """Перезагрузить тексты из JSON (для обновления без перезапуска)"""
    global _texts_cache
    _texts_cache = None
    load_texts()
    print("🔄 Тексты перезагружены")


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
