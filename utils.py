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
