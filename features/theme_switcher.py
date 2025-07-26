""" theme_switcher.py
Day/night modes
"""
# features/theme_switcher.py

from datetime import datetime

LIGHT_THEME = {
    "bg": "#F0F0F0",
    "fg": "#000000",
    "frame_bg": "#FFFFFF",
    "entry_bg": "#FFFFFF",
    "entry_fg": "#000000",
    "entry_placeholder_fg": "#888888",
    "graph_bg": "#F0F0F0",
    "button_bg": "#DDDDDD",
    "button_fg": "#000000"
}

DARK_THEME = {
    "bg": "#1E1E1E",
    "fg": "#FFFFFF",
    "frame_bg": "#2B2B2B",
    "entry_bg": "#333333",
    "entry_fg": "#FFFFFF",
    "entry_placeholder_fg": "#AAAAAA",
    "graph_bg": "#1E1E1E",
    "button_bg": "#000000",
    "button_fg": "#FFFFFF"
}

themes = [DARK_THEME, LIGHT_THEME]

def get_next_theme(current_theme):
    """
    Returns the next theme (toggles between light and dark).
    """
    if current_theme == themes[0]:
        return themes[1]
    else:
        return themes[0]

def get_default_theme():
    """
    Determines the default theme based on the current time.
    Returns LIGHT_THEME from 5 PM to 6:59 AM, else DARK_THEME.
    """
    now = datetime.now()
    if now.hour >= 17 or now.hour < 7:
        return DARK_THEME
    else:
        return LIGHT_THEME

def apply_theme(root, elements, theme):
    """
    Applies the selected theme to the UI elements.

    Parameters:
        root (tk.Tk): The main root window
        elements (dict): Dictionary of UI elements
        theme (dict): Theme dictionary to apply
    """
    root.configure(bg=theme["bg"])

    # Labels
    elements["city_label"].config(bg=theme["frame_bg"], fg=theme["fg"])
    elements["temp_label"].config(bg=theme["frame_bg"], fg=theme["fg"])
    elements["wind_label"].config(bg=theme["frame_bg"], fg=theme["fg"])
    elements["humidity_label"].config(bg=theme["frame_bg"], fg=theme["fg"])

    # Frames
    elements["current_stats_frame"].config(bg=theme["frame_bg"])
    elements["tempgraph_frame"].config(bg=theme["graph_bg"])

    # Entry
    elements["city_entry"].config(bg=theme["entry_bg"], fg=theme["entry_fg"], insertbackground=theme["entry_fg"])

    # Button
    elements["button"].config(
        bg=theme["button_bg"],
        fg=theme["button_fg"],
        activebackground=theme["button_bg"],
        activeforeground=theme["button_fg"],
        highlightbackground=theme["button_bg"],
        relief="flat",
        borderwidth=0
    )

    elements["theme_button"].config(
        bg=theme["button_bg"],
        fg=theme["button_fg"],
        activebackground=theme["button_bg"],
        activeforeground=theme["button_fg"],
        highlightbackground=theme["button_bg"],
        relief="flat",
        borderwidth=0
    )
