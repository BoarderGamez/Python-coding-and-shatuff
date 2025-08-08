from tkinter import *
import random
# AMAZING CODES WOOOOOHOOO MAKING MY WAY DOWN TOWN WALKING FAST STRANGERS PASSED AND IM HOME NOW
root = Tk()
root.title("AI Weather")
root.geometry("400x600")
root.configure(bg="#2c2c2c")

# Title
Label(root, text="AI Weather", font=("Comic Sans MS", 24, "bold"), fg="white", bg="#2c2c2c").pack(pady=10)

# 🌍 Location + Temperature Info
location_label = Label(root, text="", font=("Arial", 12), fg="lightgray", bg="#2c2c2c")
location_label.pack()

temp_frame = Frame(root, bg="#2c2c2c")
temp_frame.pack(pady=5)

temp_label = Label(temp_frame, text="", font=("Arial", 16, "bold"), fg="white", bg="#2c2c2c")
temp_label.pack()
guess_label = Label(temp_frame, text="", font=("Arial", 12), fg="lightgray", bg="#2c2c2c")
guess_label.pack()

def get_goofy_temp():
    temp = random.randint(-10, 45)
    moods = [
        "Spicy Lava Mode 🌋",
        "Penguin-Approved Chill 🐧",
        "Sweatocalypse 🔥",
        "Mild Salsa Breeze 🌶️",
        "Cloudy with a Chance of Chaos ☁️🎲",
        "Too Hot for Logic 🧠💥",
        "Weather Sponsored by Ice Cream 🍦",
        "Perfect for Lizard Sunbathing 🦎",
        "Rain Dance Required 💃🌧️"
    ]
    return f"{temp}° — {random.choice(moods)}"

def get_random_location():
    places = [
        "Banana Fjord", "Quantumville", "Cloudtopia", "Rainburg", "Sizzle City",
        "Fogtown", "Windopolis", "Sunburnt Sands", "Stormsylvania", "Mildville"
    ]
    return random.choice(places)

def get_guess_message():
    guesses = [
        "The temperature is... I think? 🤷",
        "Probably accurate-ish 🌡️",
        "Don't quote me on this 🫣",
        "Thermometer said maybe 🧪",
        "Feels like... something 🔮",
        "AI-generated weather vibes ✨"
    ]
    return random.choice(guesses)

def update_weather():
    location_label.config(text=f"Location: {get_random_location()}")
    temp_label.config(text=get_goofy_temp())
    guess_label.config(text=get_guess_message())
    root.after(3000, update_weather)

update_weather()

# 📦 Output Frame (clears on each button press)
output_frame = Frame(root, bg="#2c2c2c")
output_frame.pack(pady=10)

def clear_output():
    for widget in output_frame.winfo_children():
        widget.destroy()

# 🧪 Button Functions
def ai_forecast():
    clear_output()
    Label(output_frame, text="AI says: Buy sunglasses and a llama 🦙", fg="cyan", bg="#2c2c2c").pack()

def unlock_radar():
    clear_output()
    Label(output_frame, text="Radar unlocked! You owe us €4.99 💸", fg="orange", bg="#2c2c2c").pack()

def weather_jackpot():
    clear_output()
    outcome = random.choice(["🌈 Jackpot! Free rainbows!", "☀️ You lost. Try again!", "🌪️ Tornado loot box unlocked!"])
    Label(output_frame, text=outcome, fg="magenta", bg="#2c2c2c").pack()

def get_likes():
    clear_output()
    likes = random.randint(1, 9999)
    Label(output_frame, text=f"You got {likes} likes for rain! 👍", fg="lightgreen", bg="#2c2c2c").pack()

# 🎮 Buttons
Button(root, text="Get AI Forecast 💡", command=ai_forecast, bg="#ff69b4", fg="white", font=("Arial", 12)).pack(pady=5)
Button(root, text="Unlock Detailed Radar 💰", command=unlock_radar, bg="#00ced1", fg="white", font=("Arial", 12)).pack(pady=5)
Button(root, text="Play Weather Jackpot 🎰", command=weather_jackpot, bg="#dda0dd", fg="white", font=("Arial", 12)).pack(pady=5)
Button(root, text="Get Likes for Rain 👍", command=get_likes, bg="#1e90ff", fg="white", font=("Arial", 12)).pack(pady=5)

# 🧭 Navigation Icons
nav_frame = Frame(root, bg="#2c2c2c")
nav_frame.pack(side=BOTTOM, pady=20)
for icon in ["🏠", "📊", "❓"]:
    Label(nav_frame, text=icon, font=("Arial", 20), fg="gray", bg="#2c2c2c", padx=20).pack(side=LEFT)
print("AI Weather Apfp is rIf you fly awayunning...")
root.mainloop()
