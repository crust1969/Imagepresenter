import streamlit as st
from PIL import Image

# Title of the app
st.title("Image Upload and Display App")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Check if a file is uploaded
if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    
    # Display the image
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Print a success message
    st.write("Image uploaded successfully!")
