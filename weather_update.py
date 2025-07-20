"""
weather_update.py

Handles coordination between weather data retrieval (via weather_api.py)
and updating the UI components in the Tkinter dashboard.
"""

from weather_api import get_current_weather
from features.temperature_graph import plot_temperature_history
from tkinter import messagebox
from weather_api import get_daily_avg_temps
from features.weather_history import save_daily_weather, calculate_average_temperature, get_recent_temperatures
import requests

def update_weather(city, city_label, temp_label, wind_label, humidity_label, tempgraph_frame):
    """
    Fetches weather data for the given city and updates the Tkinter UI.

    Parameters:
        city (str): The city name to fetch weather data for.
        city_label (tk.Label): Label widget to display the city name.
        temp_label (tk.Label): Label widget to display the temperature.
        wind_label (tk.Label): Label widget to display wind details.
        tempgraph_frame (tk.Frame): Frame widget to display the temperature graph.

    Returns:
        None
    """
    try:
        current = get_current_weather(city)

        # update labels
        city_label.config(text=city)
        temp_f = current["main"]["temp"]
        temp_label.config(text=f"{temp_f:.1f}°F ± 3")

        wind = current["wind"]
        wind_dir = deg_to_compass(wind['deg'])
        wind_label.config(text=f"Wind: {wind_dir}, {wind['speed']} mph")

        humidity = current["main"]["humidity"]
        humidity_label.config(text=f"Humidity: {humidity}%")

        # save today's data to CSV
        save_daily_weather(city, temp_f)

        # Try getting 7 days from CSV
        df = get_recent_temperatures(city, 7)
        if len(df) == 7:
            temps = df["temperature"].tolist()[::-1]
            title = f"{city.title()} Avg Temp (Last 7 Days)"
        else:
            temps = get_daily_avg_temps(city)
            title = f"{city.title()} Avg Temp (Last 5 Days)"


        plot_temperature_history(tempgraph_frame, temps, title)

    
    # error handling for issues during weather data fetching
    except requests.exceptions.HTTPError as http_err:
        status_code = http_err.response.status_code
        if status_code == 404:
            messagebox.showerror("City Not Found", "Sorry, we couldn't find weather data for that city. Please check your spelling and try again.")
        elif status_code == 401:
            messagebox.showerror("Unauthorized", "There seems to be an issue with the API key. Please verify it is set correctly.")
        else:
            messagebox.showerror("Error", f"An HTTP error occurred: {status_code}")
    except requests.exceptions.RequestException:
        messagebox.showerror("Connection Error", "Network problem. Please check your internet connection.")
    except Exception as e:
        print(f"LINE 74 Unexpected error: {e}")
        messagebox.showerror("Error", "An unexpected error occurred while fetching weather data.")

# convert degrees to compass direction
def deg_to_compass(deg):
    directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                  'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    ix = int((deg + 11.25) / 22.5) % 16
    return directions[ix]