import tkinter as tk
from features.temperature_graph import plot_temperature_history

root = tk.Tk()
root.title("Weather App")
root.geometry("1000x600")
root.configure(bg="#1E1E1E") # set the background to dark mode

# allow resizing of grid
root.grid_columnconfigure(0, weight=0) # sidebar is fixed, wont resize
root.grid_columnconfigure(1, weight=1) # graph will resize
root.grid_rowconfigure(0, weight=0)  # title stays fixed height
root.grid_rowconfigure(1, weight=1) 

label = tk.Label(root, text="Weather Dashboard", font="Helvetica 16", fg="white", bg="#1E1E1E")
# anchor title to the top left corner
label.grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=(10, 20))

# Create a frame for the weather data
current_stats_frame = tk.Frame(root, width=180, bg="#2B2B2B")
current_stats_frame.grid(row=1, column=0, sticky="n", padx=20, pady=20) # place sidebar below title
current_stats_frame.grid_propagate(False) # prevent frame from resizing

# Sample labels to test layout of frame
city_label = tk.Label(current_stats_frame, text="New York City", fg="#FFFFFF", bg="#2B2B2B", font=("Helvetica", 12))
city_label.pack(pady=(10,5))

temp_label = tk.Label(current_stats_frame, text="70°F ± 3", fg="#D3D3D3", bg="#2B2B2B", font=("Helvetica", 16, "bold"))
temp_label.pack(pady=5)

wind_label = tk.Label(current_stats_frame, text="Wind: WSW 6 mph", fg="#AAAAAA", bg="#2B2B2B", font=("Helvetica", 10))
wind_label.pack(pady=(5, 15))

# create frame for temperature graph
tempgraph_frame = tk.Frame(root, bg="#1E1E1E")
tempgraph_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
tempgraph_frame.pack_propagate(False) # widgets in frame can expand

# test layout with dummy date
dummy_weekly_temps = [70, 68, 71, 74, 77, 75, 72]
plot_temperature_history(tempgraph_frame, dummy_weekly_temps)


root.mainloop()

def fake_fetch_weather():
    label.config(text="Portland: 72°F, Sunny")

button = tk.Button(root, text="Get Weather", command=fake_fetch_weather)
button.grid(row=2, column=0, sticky="w", padx=20, pady=(0, 20))
