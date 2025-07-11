import streamlit as st

def home_page():
    
    st.markdown(
    """
    <style>
    /* Apply background image to the main content area */
    .main {
        background-image: url('https://www.ecowatch.com/wp-content/uploads/2021/10/1597324057-origin.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-color: rgba(255, 255, 255, 0.6);
        background-blend-mode: overlay; 
        padding: 0px;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    # Center the image
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://cdni.iconscout.com/illustration/premium/thumb/farmers-with-fruit-trolley-illustration-download-in-svg-png-gif-file-formats--carrying-the-pumpkin-cart-man-pushing-farmer-pack-agriculture-illustrations-6020568.png?f=webp" style="max-width: 90%;">
        </div>
        """,
        unsafe_allow_html=True
    )
