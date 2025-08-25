# weather.py
import requests

def get_weather(city):
    response = requests.get(f"https://api.weather.com/{city}")
    return response.json()