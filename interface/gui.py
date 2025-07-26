"""interface/gui.py

Creates and manages the Tkinter GUI for the weather dashboard, including layout, input, and display widgets.
"""

import tkinter as tk
from tkinter import messagebox
from features.temperature_graph import plot_temperature_history
from features.theme_switcher import apply_theme,get_default_theme, get_next_theme


def create_dashboard(update_callback):
    """Builds Tkinter UI and returns root and key UI elements."""
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("1000x600")
    # root.configure(bg="#1E1E1E") # set the background to dark mode

    theme = get_default_theme()

    # grid config - allow resizing of grid
    root.grid_columnconfigure(0, weight=0) # sidebar is fixed, wont resize
    root.grid_columnconfigure(1, weight=1) # graph will resize
    root.grid_rowconfigure(0, weight=0) # title stays fixed height
    root.grid_rowconfigure(1, weight=1)

    # title
    label = tk.Label(root, text="Weather Dashboard", font="Helvetica 16")
    label.grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=(10, 20))

    # sidebar
    current_stats_frame = tk.Frame(root, width=180)
    current_stats_frame.grid(row=1, column=0, sticky="n", padx=20, pady=20) # place sidebar below title
    current_stats_frame.grid_propagate(False) # prevent frame from resizing

    # default labels to test layout of frame
    city_label = tk.Label(current_stats_frame, text="Please Enter a City!", font=("Helvetica", 12))
    city_label.pack(pady=(10, 5))

    temp_label = tk.Label(current_stats_frame, text="", font=("Helvetica", 16, "bold"))
    temp_label.pack(pady=5)

    wind_label = tk.Label(current_stats_frame, text="", font=("Helvetica", 10))
    wind_label.pack(pady=(5, 15))
    
    humidity_label = tk.Label(current_stats_frame, text="", font=("Helvetica", 10))
    humidity_label.pack(pady=(5, 15))

    # graph area
    tempgraph_frame = tk.Frame(root)
    tempgraph_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
    tempgraph_frame.pack_propagate(False)

    # city input
    placeholder = "Enter City Name"
    city_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
    city_entry.insert(0, placeholder)
    city_entry.grid(row=2, column=0, sticky="w", padx=20, pady=(0, 20))

    def usertyping(event=None):
        """Clears placeholder text and changes font color when user begins typing."""
        if city_entry.get() == placeholder:
            city_entry.delete(0, tk.END)  # clear placeholder text
            city_entry.config(fg=theme["entry_fg"])

    def on_focus_out(event=None):
        """Restores placeholder text if the input field is left empty on focus out."""
        if city_entry.get() == "":
            city_entry.insert(0, placeholder)
            city_entry.config(fg=theme["entry_placeholder_fg"])

    city_entry.bind("<FocusIn>", usertyping)
    city_entry.bind("<FocusOut>", on_focus_out)
    
    def on_click():
        """Event happens when 'Get Weather' button is clicked, validates input, and triggers weather update."""
        city = city_entry.get().strip()
        if city == placeholder or not city:
            messagebox.showwarning("Input Error", "Please enter a valid city name.")
            return
        else:
            update_callback(city, city_label, temp_label, wind_label, humidity_label, tempgraph_frame)  # call the update function with the city name


    # refresh button
    button = tk.Button(
        root,
        text="Get Weather",
        command=on_click,
        bg=theme["button_bg"],
        fg=theme["button_fg"],
        activebackground=theme["button_bg"],
        activeforeground=theme["button_fg"],
        highlightbackground=theme["button_bg"],
        relief="flat",
        borderwidth=0
    )

    button.grid(row=2, column=0, sticky="e", padx=20, pady=(0, 20))

    theme_button = tk.Button(
        root,
        text="Toggle Theme",
        bg=theme["button_bg"],
        fg=theme["button_fg"],
        activebackground=theme["button_bg"],
        activeforeground=theme["button_fg"],
        highlightbackground=theme["button_bg"],
        relief="flat",
        borderwidth=0
    )
    theme_button.grid(row=2, column=1, sticky="e", padx=20, pady=(0, 20))

    elements = {
        "root": root,
        "city_label": city_label,
        "temp_label": temp_label,
        "wind_label": wind_label,
        "humidity_label": humidity_label,
        "current_stats_frame": current_stats_frame,
        "tempgraph_frame": tempgraph_frame,
        "city_entry": city_entry,
        "button": button,
        "theme_button": theme_button,
        "title_label": label
    }

    apply_theme(root, elements, theme)

    def toggle_theme():
        nonlocal theme
        theme = get_next_theme(theme)
        apply_theme(root, elements, theme)

    theme_button.config(command=toggle_theme)

    return root, city_label, temp_label, wind_label, humidity_label, tempgraph_frame, theme_button
