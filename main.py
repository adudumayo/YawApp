import os
import requests

def get_weather(city):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None
    
weather_data = get_weather('Durban')

if weather_data:
    weather = weather_data.get('weather')
    print(weather_data)
else:
    print("This is iteration one")