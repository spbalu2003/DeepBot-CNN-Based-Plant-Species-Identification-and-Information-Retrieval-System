import streamlit as st
import pandas as pd
def plants_page():
    # Center the login form using Streamlit form layout
    st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://media.architecturaldigest.com/photos/651dae9b1fb323efb7c1fe4b/master/w_1600%2Cc_limit/GettyImages-1404287433.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            min-height: 100vh;  /* Ensure the background covers the whole screen */
            background-color: rgba(255, 255, 255, 0.6); /* Add a semi-transparent overlay */
            background-blend-mode: overlay; /* Blend the image with the overlay */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    data=pd.read_csv('image_labels.csv')
    labels = data['Label'].unique()
    

    # Create a layout with 3 columns
    cols = st.columns(3)

    # Loop through unique labels and display them in styled boxes
    for idx, label in enumerate(labels):
        col = cols[idx % 3]  # Distribute labels across 3 columns
        col.markdown(
            f"""
            <div style="text-align: center; padding: 10px; background-color: rgba(135, 206, 235, 0.7); border-radius: 15px; border: 1.5px solid black; margin-bottom: 10px;">
                <p style="color: black; font-size: 20px;"><b>{label}</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )
