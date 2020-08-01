import requests


def forecast(city_name: str = 'Moscow', lat: float = None, lon: float = None) -> dict:
    if (lat and lon) is not None:
        city_name = None

    url = 'https://api.openweathermap.org/data/2.5/weather'
    # noinspection SpellCheckingInspection
    params = {
        'lon': lon,
        'lat': lat,
        'q': city_name,
        'appid': '11c0d3dc6093f7442898ee49d2430d20',
        'units': 'metric',
        'lang': 'ru'
    }

    resp = requests.get(url, params=params).json()

    wind = resp['wind']['deg']
    wind_type = str
    if 11.26 <= wind <= 33.75:
        wind_type = "ССВ"
    elif 33.76 <= wind <= 56.25:
        wind_type = "СВ"
    elif 56.26 <= wind <= 78.75:
        wind_type = "ВСВ"
    elif 78.76 <= wind <= 101.25:
        wind_type = "В"
    elif 101.26 <= wind <= 123.75:
        wind_type = "ВЮВ"
    elif 123.76 <= wind <= 146.25:
        wind_type = "ЮВ"
    elif 146.26 <= wind <= 168.75:
        wind_type = "ЮЮВ"
    elif 168.76 <= wind <= 191.25:
        wind_type = "Ю"
    elif 191.25 <= wind <= 213.75:
        wind_type = "ЮЮЗ"
    elif 213.76 <= wind <= 236.25:
        wind_type = "ЮЗ"
    elif 236.26 <= wind <= 258.75:
        wind_type = "ЗЮЗ"
    elif 258.76 <= wind <= 281.25:
        wind_type = "З"
    elif 281.26 <= wind <= 303.75:
        wind_type = "ЗСЗ"
    elif 303.76 <= wind <= 326.25:
        wind_type = "ЗС"
    elif 326.26 <= wind <= 348.75:
        wind_type = "ССЗ"
    else:
        wind_type = "С"

    wind_speed = resp['wind']['speed']

    city = resp['name']

    temp = round(resp['main']['temp'], 1)

    desc = resp['weather'][0]['description']

    humid = resp['main']['humidity']

    torr = 101325 / 760 / 100
    pressure = round(resp['main']['pressure'] / torr)

    print(f"{city} - {temp} C, {desc}, влажность - {humid}%, атмосферное давление - "
          f"{pressure} мм.рт.ст., ветер - {wind_type} {wind_speed} м/c\n")

    return resp


forecast()
forecast(city_name='Керва')
forecast(city_name='Орел')
forecast(city_name='Аделаида')
forecast(lat=90, lon=0)  # Северный полюс
forecast(lat=0, lon=0)  # Экватор (нулевая координата)
forecast(lat=-90, lon=0)  # Южный полюс
