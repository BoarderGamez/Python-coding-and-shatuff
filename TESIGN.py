import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Create window
root = tk.Tk()
root.title("Yassified Weather App")
root.geometry("360x760")
root.configure(bg="#bfb3d9")  # Light purple background for ✨vibes✨

# Load the main background image
bg_img = Image.open("/mnt/data/Screenshot 2025-08-08 192313.png")
bg_img = bg_img.resize((360, 760))
bg_photo = ImageTk.PhotoImage(bg_img)

# Background label
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Weather info block
weather_frame = tk.Frame(root, bg="#00000080", bd=0)
weather_frame.place(x=20, y=20, width=320, height=160)

tk.Label(weather_frame, text="Aircraft Wing", fg="white", bg="#00000000", font=("Helvetica", 16)).pack(pady=(10,0))
tk.Label(weather_frame, text="Deth", fg="white", bg="#00000000", font=("Helvetica", 36, "bold")).pack()
tk.Label(weather_frame, text="Quite Breezy, henny", fg="white", bg="#00000000", font=("Helvetica", 12)).pack()
tk.Label(weather_frame, text="H: 50°  L: -50°", fg="white", bg="#00000000", font=("Helvetica", 12)).pack()

# Tabs for forecast
tab_frame = tk.Frame(root, bg="#7e57c2", bd=0)
tab_frame.place(x=0, y=600, width=360, height=160)

ttk.Style().configure("TNotebook.Tab", padding=[10, 5], font=("Helvetica", 10, "bold"))
notebook = ttk.Notebook(tab_frame)
notebook.pack(expand=1, fill="both")

hourly_tab = tk.Frame(notebook, bg="#4a148c")
weekly_tab = tk.Frame(notebook, bg="#6a1b9a")

notebook.add(hourly_tab, text="Hourly Forecast")
notebook.add(weekly_tab, text="Weekly Forecast")

# Hourly Forecast Details
tk.Label(hourly_tab, text="12 AM", bg="#4a148c", fg="white", font=("Helvetica", 12)).place(x=20, y=10)
tk.Label(hourly_tab, text="🌧️ 100%\n50°", bg="#4a148c", fg="white", font=("Helvetica", 10)).place(x=20, y=40)

tk.Label(hourly_tab, text="Now", bg="#4a148c", fg="white", font=("Helvetica", 12)).place(x=100, y=10)
tk.Label(hourly_tab, text="🌧️\n-50°", bg="#4a148c", fg="white", font=("Helvetica", 10)).place(x=100, y=40)

# Lock image placeholder
lock_canvas = tk.Canvas(hourly_tab, width=60, height=60, bg="white", highlightthickness=0)
lock_canvas.create_oval(10, 10, 50, 50, outline="gold", width=4)
lock_canvas.place(x=200, y=10)

# EA + Bitcoin (basic simulation)
tk.Label(hourly_tab, text="EA\nSPORTS", bg="#4a148c", fg="red", font=("Helvetica", 10, "bold")).place(x=280, y=10)
tk.Label(hourly_tab, text="$ 500\n₿", bg="#4a148c", fg="orange", font=("Helvetica", 12)).place(x=280, y=50)

root.mainloop()
