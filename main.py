"""
main.py

Initialized Weather Dashboard application.

- Initializes Tkinter GUI via the create_dashboard function from interface.gui.
- Connects the user interface to the update_weather logic from weather_update file.
- Triggers initial weather fetch using default city ("New York").
- Starts the Tkinter main event loop.

Functions:
    - updatewd(city): Wrapper function that passes required widgets and city to update_weather.

Returns:
    None
"""
from interface.gui import create_dashboard
from weather_update import update_weather

def updatewd(city="New York"):
    update_weather(city, city_label, temp_label, wind_label, humidity_label, tempgraph_frame)

# Create full UI and get key widgets
root, city_label, temp_label, wind_label, humidity_label, tempgraph_frame, theme_button = create_dashboard(update_weather)

# Trigger initial load
updatewd()  # Default city

# Run app
root.mainloop()
