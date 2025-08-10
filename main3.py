import streamlit as st
from PIL import Image

# Load and display the screenshot
image = Image.open("screenshot_2025-08-08.png")  # Adjust path if needed
st.image(image, caption="Screenshot from August 8, 2025", use_column_width=True)
