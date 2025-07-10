import requests
from config import api_key  # import api key from config.py
from collections import defaultdict # needed for temperature graph data
from datetime import datetime # sorting dates in temperature graph

BASE_URL = "https://api.openweathermap.org/data/2.5"

def get_current_weather(city, units="imperial"):
    """gets current weather data for a given city."""
    params = {
        "q": city,
        "appid": api_key,
        "units": units
    }
    resp = requests.get(f"{BASE_URL}/weather", params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()

def get_5day_forecast(city, units="imperial"):
    """gets 5-day forecast in 3-hour intervals for city."""
    params = {
        "q": city,
        "appid": api_key,
        "units": units
    }
    resp = requests.get(f"{BASE_URL}/forecast", params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()

def get_daily_avg_temps(city, units="imperial"):
    """Returns a list of average daily temps for the next 5 days for given city."""
    forecast_data = get_5day_forecast(city, units)
    temps_by_day = defaultdict(list)

    for entry in forecast_data["list"]:
        # extract date from timestamp in datetime format
        date_str = entry["dt_txt"].split()[0]
        temps_by_day[date_str].append(entry["main"]["temp"])

    # compute average temp per day
    daily_avgs = []
    for day in sorted(temps_by_day.keys())[:5]:  # limit to next 5 days given free API tier limitations
        temps = temps_by_day[day]
        avg_temp = sum(temps) / len(temps)
        daily_avgs.append(round(avg_temp, 1))

    return daily_avgs


# test block:
if __name__ == "__main__":
    data = get_current_weather("New York")
    print(data)