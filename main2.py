import streamlit as st
from datetime import datetime

# Title and Header
st.set_page_config(page_title="WingCast", layout="centered")
st.title("✈️ WingCast: Weather from the Aircraft Wing")
st.subheader("Quite Breezy, H:50°, L:30°")

# Images (placeholder URLs or local files)
st.image("https://via.placeholder.com/300x200?text=Person+on+Wing", caption="Live from the Wing")
st.image("https://via.placeholder.com/300x200?text=Aircraft+Wing+View", caption="View from Above")

# Hourly Forecast
st.markdown("### 🌡️ Hourly Forecast")
current_time = datetime.now().strftime("%I:%M %p")
st.write(f"Current Time: {current_time}")
st.write("12 AM: 50°F")
st.write("Now: -50°F ❄️ (Definitely not accurate)")

# Weekly Forecast (mocked)
st.markdown("### 📅 Weekly Forecast")
forecast = {
    "Mon": "🌧️ 45°F",
    "Tue": "☀️ 60°F",
    "Wed": "🌬️ 30°F",
    "Thu": "🌩️ 50°F",
    "Fri": "❄️ -10°F",
}
for day, temp in forecast.items():
    st.write(f"{day}: {temp}")

# Microtransactions Section
st.markdown("### 💸 Microtransactions")
st.image("https://via.placeholder.com/50x50?text=🔒", caption="Unlock Premium Forecast")
st.image("https://via.placeholder.com/50x50?text=EA", caption="EA Weather Pack")
st.image("https://via.placeholder.com/50x50?text=₿", caption="Bitcoin Weather Boost - $500")

# Footer
st.markdown("---")
st.caption("This app is a parody. Do not trust it for actual weather updates.")

