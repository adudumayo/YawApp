import requests

def get_weather(city):
    api_key = 'the api key here'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None
    
weather_data = get_weather('Durban')
print(weather_data)