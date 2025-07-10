from interface.gui import create_dashboard
from weather_update import update_weather

def updatewd(city="New York"):
    update_weather(city, city_label, temp_label, wind_label, humidity_label, tempgraph_frame)

# Create full UI and get key widgets
root, city_label, temp_label, wind_label, humidity_label, tempgraph_frame = create_dashboard(update_weather)

# Trigger initial load
updatewd()  # Default city

# Run app
root.mainloop()
