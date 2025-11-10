def get_weather():
    import requests
    
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
                'wind_speed': wind_speed
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
            _texts_cache = json.load(file)
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
