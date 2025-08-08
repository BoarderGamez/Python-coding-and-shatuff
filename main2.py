import streamlit as st
import random

st.set_page_config(page_title="main2", page_icon="🌤️", layout="centered")

# 🎨 Styling
st.markdown("""
    <style>
        .main {background-color: #2c2c2c;}
        h1, h2, p {color: white;}
        .stButton>button {background-color: #ff69b4; color: white;}
    </style>
""", unsafe_allow_html=True)

# 🏷️ Title
st.markdown("<h1 style='text-align: center;'>main2</h1>", unsafe_allow_html=True)

# 🌍 Location + Temperature Info
def get_goofy_temp():
    temp = random.randint(-10, 45)
    moods = [
        "Spicy Lava Mode 🌋", "Penguin-Approved Chill 🐧", "Sweatocalypse 🔥",
        "Mild Salsa Breeze 🌶️", "Cloudy with a Chance of Chaos ☁️🎲",
        "Too Hot for Logic 🧠💥", "Weather Sponsored by Ice Cream 🍦",
        "Perfect for Lizard Sunbathing 🦎", "Rain Dance Required 💃🌧️"
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
        "The temperature is... I think? 🤷", "Probably accurate-ish 🌡️",
        "Don't quote me on this 🫣", "Thermometer said maybe 🧪",
        "Feels like... something 🔮", "AI-generated weather vibes ✨"
    ]
    return random.choice(guesses)

# 🔄 Weather Update
if st.button("🔄 Refresh Weather"):
    st.subheader(f"Location: {get_random_location()}")
    st.write(get_goofy_temp())
    st.caption(get_guess_message())

# 📦 Output Actions
st.markdown("---")
st.subheader("🎮 Weather Actions")

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
st.markdown("<h2 style='text-align: center;'>🏠 📊 ❓</h2>", unsafe_allow_html=True)
