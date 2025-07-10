"""
    Function plot_temperature_history plots average daily temperature data for the past 5 days using Matplotlib and embeds the chart in a Tkinter frame.

    Parameters:
        frame (tk.Frame): The Tkinter frame where the graph should be displayed.
        temperature_data (list of float): A list of temperature values for each day.

    Returns:
        None
    """

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta

def plot_temperature_history(frame, temperature_data):
    fig, ax = plt.subplots(figsize=(6, 3), dpi=100)
    ax.plot(temperature_data, color='orange', marker='o')

    # set x-ticks to past 5 days
    labels = [
        (datetime.today() - timedelta(days=len(temperature_data)-1-i)).strftime("%a")
        for i in range(len(temperature_data))
    ]
    ax.set_xticks(range(len(temperature_data)))
    ax.set_xticklabels(labels, color='white')

    # set axis labels and titles
    ax.set_title("Average Daily Temperature (Past 5 Days)", color='white', pad=10, fontsize=10, fontweight='bold')
    ax.set_ylabel("°F", color='white')
    ax.set_xlabel("Day", color='white')
    ax.tick_params(colors='white')
    ax.set_facecolor("#1E1E1E")
    fig.patch.set_facecolor("#1E1E1E")
    fig.tight_layout(pad=2)
    ax.grid(True)

    # clear previous graph
    for widget in frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

