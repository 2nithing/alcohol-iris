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
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Mock processing: resizing and normalization (adjust as needed)
    resized_img = cv2.resize(gray, (128, 128))
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

# Streamlit UI Enhancements
st.set_page_config(page_title="Sober Iris Detection", page_icon="👁️", layout="centered")
st.markdown("""
    <style>
        .stApp {
            background-color: #f0f2f6;
        }
        .title-text {
            font-size: 30px;
            font-weight: bold;
            text-align: center;
            color: #4a4a4a;
        }
        .upload-box {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<p class='title-text'>🚗 Sober Iris Detection System</p>", unsafe_allow_html=True)
st.write("Detect sobriety based on iris patterns to prevent drunk driving.")

# Upload Image Section
st.markdown("### 📤 Upload an Iris Image")
image_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"], help="Upload a clear image of the eye.")

if image_file is not None:
    st.markdown("### 🖼️ Uploaded Image")
    st.image(load_image(image_file), caption='Iris Image', use_column_width=True)
    
    if st.button("🔍 Analyze", key="analyze_button", help="Click to analyze the image"):
        # Preprocess and predict
        img = load_image(image_file)
        processed_img = preprocess_image(img)
        result = predict_sobriety(processed_img)
        
        st.markdown("### 📌 Result")
        st.success(f"The person is: **{result}**")
