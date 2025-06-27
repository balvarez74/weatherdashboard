import tkinter as tk

root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

label = tk.Label(root, text="Welcome to my Weather App")
label.pack(pady=20)

root.mainloop()

def fake_fetch_weather():
    label.config(text="Portland: 72°F, Sunny")

button = tk.Button(root, text="Get Weather", command=fake_fetch_weather)
button.pack()
