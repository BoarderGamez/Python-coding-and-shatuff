import streamlit as st
import random

st.set_page_config(page_title="AI Weather", layout="centered", page_icon="🌦️")

st.title("AI Weather")
st.markdown("#### Making my way downtown... 🌆")

# 🌍 Location + Temperature Info
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

# Display Weather Info
location = get_random_location()
temperature = get_goofy_temp()
guess = get_guess_message()

st.markdown(f"**Location:** {location}")
st.markdown(f"**Temperature:** {temperature}")
st.markdown(f"**Guess:** {guess}")

# 📦 Output Section
st.markdown("---")
st.subheader("AI Weather Actions")

if st.button("Get AI Forecast 💡"):
    st.success("AI says: Buy sunglasses and a llama 🦙")

if st.button("Unlock Detailed Radar 💰"):
    st.warning("Radar unlocked! You owe us €4.99 💸")

if st.button("Play Weather Jackpot 🎰"):
    outcome = random.choice([
        "🌈 Jackpot! Free rainbows!",
        "☀️ You lost. Try again!",
        "🌪️ Tornado loot box unlocked!"
    ])
    st.info(outcome)

if st.button("Get Likes for Rain 👍"):
    likes = random.randint(1, 9999)
    st.success(f"You got {likes} likes for rain! 👍")

# 🧭 Navigation Icons
st.markdown("---")
st.markdown("🏠 📊 ❓")

