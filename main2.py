import streamlit as st
import os

# Define the absolute paths to images
images = [
    os.path.abspath('/workspaces/Python-coding-and-shatuff/Screenshot 2025-08-08 192313.png'),
    os.path.abspath('/workspaces/Python-coding-and-shatuff/Unbenannt.png'),
]

# Set up a session state to keep track of the image index
if 'image_index' not in st.session_state:
    st.session_state.image_index = 0

# Function to navigate images
def next_image():
    st.session_state.image_index = (st.session_state.image_index + 1) % len(images)

def previous_image():
    st.session_state.image_index = (st.session_state.image_index - 1) % len(images)

# Display the current image
try:
    st.image(images[st.session_state.image_index], caption=f"Image {st.session_state.image_index + 1}", use_column_width=True)
except Exception as e:
    st.error(f"An error occurred while loading the image: {e}")

# Image navigation
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button('Previous'):
        previous_image()

with col3:
    if st.button('Next'):
        next_image()