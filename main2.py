import streamlit as st

# List of image file paths
images = [
    '/workspaces/Python-coding-and-shatuff/Screenshot 2025-08-08 192313.png',
    '/workspaces/Python-coding-and-shatuff/Unbenannt.png',
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
st.image(images[st.session_state.image_index])

# Image navigation
col1, col2, col3 = st.columns([1,2,1])
with col1:
    if st.button('Previous'):
        previous_image()

with col3:
    if st.button('Next'):
        next_image()