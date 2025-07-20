"""
daily_weather_pull.py

Handles daily weather data retrieval (via get_current_weather.py)
and saves the data to a CSV file for historical tracking.

"""

from weather_api import get_current_weather
from features.weather_history import save_daily_weather

CITIES = ["New York", "Lakeland"]

def daily_weather_pull():
    for city in CITIES:
        try:
            weather = get_current_weather(city)
            temp_f = weather["main"]["temp"]
            save_daily_weather(city, temp_f)
        except Exception as e:
            print(f"Failed to fetch and/or save data for {city}: {e}")

if __name__ == "__main__":
    daily_weather_pull()
