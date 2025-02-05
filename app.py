import streamlit as st
import cv2
from PIL import Image, ImageOps
import numpy as np

def load_image(image_file):
    img = Image.open(image_file)
    return img

def preprocess_image(image):
    # Convert PIL image to OpenCV format
    img = np.array(image)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Mock processing: resizing and normalization (adjust as needed)
    resized_img = cv2.resize(img, (128, 128))
    normalized_img = resized_img / 255.0
    return normalized_img

# Mock function for prediction
def predict_sobriety(processed_image):
    # In real implementation, load model and predict here
    # Mock prediction for demonstration
    if np.mean(processed_image) > 0.5:
        return "Sober"
    else:
        return "Drunk"

st.title("Sober Iris Detection System")
st.write("Upload an iris image to determine if the individual is sober or drunk.")

image_file = st.file_uploader("Upload Iris Image", type=["jpg", "jpeg", "png"])

if image_file is not None:
    st.image(load_image(image_file), caption='Uploaded Iris Image', use_container_width=True)
    
    if st.button("Analyze"):
        # Preprocess and predict
        img = load_image(image_file)
        processed_img = preprocess_image(img)
        result = predict_sobriety(processed_img)
        
        st.subheader("Result")
        st.write(f"The person is: {result}")
