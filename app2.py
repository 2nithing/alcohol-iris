import streamlit as st
from PIL import Image
import numpy as np

# Custom CSS for professional styling
st.markdown(
    """
    <style>
    .header {
        font-size: 40px;
        font-weight: bold;
        color: #2E86C1;
        text-align: center;
        padding: 20px;
    }
    .description {
        font-size: 18px;
        color: #34495E;
        text-align: center;
        padding: 10px;
    }
    .upload-section {
        background-color: #F2F3F4;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    .result-section {
        background-color: #EAEDED;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    .result-text {
        font-size: 24px;
        font-weight: bold;
        color: #2E86C1;
        text-align: center;
    }
    .column-style {
        padding: 20px;
        border-radius: 10px;
        background-color: #FFFFFF;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Section
st.markdown('<div class="header">Drug Detection App</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="description">Upload an iris image to detect if the person is under the influence of drugs.</div>',
    unsafe_allow_html=True,
)

# Image Upload Section
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload an iris image", type=["jpg", "jpeg", "png"])
st.markdown('</div>', unsafe_allow_html=True)

# Two-Column Layout
if uploaded_file is not None:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.markdown("**Uploaded Image**")
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Iris Image", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.markdown("**Analysis Results**")

        # Placeholder for ML model prediction
        # Replace this with your actual ML model prediction logic
        def predict_drug_effect(image):
            # Example: Random prediction for demonstration
            return np.random.choice(["Not Under Drug Effect", "Under Drug Effect"])

        # Convert image to numpy array for processing
        image_np = np.array(image)
        prediction = predict_drug_effect(image_np)

        # Display the result
        st.markdown('<div class="result-section">', unsafe_allow_html=True)
        st.markdown(f'<div class="result-text">Prediction: {prediction}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Additional details (optional)
        st.markdown("**Confidence Level:** 85%")  # Replace with actual confidence from your model
        st.markdown("**Analysis Time:** 2.3 seconds")  # Replace with actual processing time
        st.markdown('</div>', unsafe_allow_html=True)