import requests
import json

def fetch_weather(api_key, city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = f"{base_url}q={city}&appid={api_key}"

    response = response.get(complete_url)

    if response.status.code == 200:
        data = response.json()

        main = data['main']
        temparature = main['temp']
        humidity = main['humidity']

        return weather_data
    
    else:
        print('It failed')
        return None
    
api_key = 'your_openweather_api_key_here'
city = 'San Francisco'
weather_data = fetch_weather(api_key, city)

