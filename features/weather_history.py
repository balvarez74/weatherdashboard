"""
weather_history.py

Handles saving and retrieving historical weather data from a CSV file.
Used to display and calculate 7-day and 30-day temperature trends.
"""

import csv
import os
from datetime import datetime, timedelta
import pandas as pd


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "..", "weather_history.csv")

def save_daily_weather(city, temp_f):
    """
    Saves today's weather data for the specified city to CSV,
    only if it hasn't already been saved.
    """
    today = datetime.today().strftime("%Y-%m-%d")

    # Check if file exists and today's entry for the city already exists
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2 and row[0] == today and row[1].lower() == city.lower():
                    print("Today's weather already saved for this city.")
                    return

    # Append new data
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([today, city, round(temp_f, 1)])
        print(f"Weather saved to CSV for {city}")


def get_recent_temperatures(city, days=7):
    """
    Retrieves recent temperature data for a given city from the CSV file.

    Parameters:
        city (str): City name to filter data for.
        days (int): Number of recent days to return.

    Returns:
        pd.DataFrame: Filtered DataFrame with 'date' and 'temperature' columns.
    """
    try:
        df = pd.read_csv(CSV_FILE, header=None, names=["date", "city", "temperature"])
        df["date"] = pd.to_datetime(df["date"])
        df["city"] = df["city"].astype(str).str.strip()  # Ensure city column is treated as string
        df = df[df["city"].astype(str).str.lower() == str(city).lower()]
        cutoff_date = datetime.today() - timedelta(days=int(days))
        df = df[df["date"] >= cutoff_date]
        df = df.sort_values("date")

        return df[["date", "temperature"]].reset_index(drop=True)
    except Exception as e:
        print("Error reading CSV:", e)
        return pd.DataFrame(columns=["date", "temperature"])


def calculate_average_temperature(days=7, city=None):
    """
    Returns the average temperature over the last `days` saved records.
    """
    df = get_recent_temperatures(city=city, days=days)
    if df.empty:
        return None
    return round(df["temperature"].mean(), 1)
