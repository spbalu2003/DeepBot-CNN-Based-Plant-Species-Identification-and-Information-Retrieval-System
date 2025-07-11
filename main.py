import streamlit as st
from prediction_page import prediction_page
from streamlit_option_menu import option_menu
from home_page import home_page
from plants_page import plants_page
from about_page import about_us_page
# Streamlit Page Config
st.set_page_config(page_title = 'Plant Species', layout='wide', page_icon="🌿")

# Add background image to the main page



# Session State Initialization
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

if st.session_state["page"] == "Home":
    # Horizontal navigation for non-logged-in users
    st.markdown(
        """
        <div style="text-align: center; padding: 1px; background-color: rgba(255, 99, 71, 0.4); border-radius: 40px; border: 1.5px solid black; margin-bottom: 20px;">
            <p style="color: black; font-size: 40px;"><b>DeepBot: CNN-Based Plant Species Identification and Information Retrieval System</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )
    selected_page = option_menu(
        menu_title=None,
        options=["Home", "Predictions", "Plants Data",'Recommendations'],
        icons=["house", "cloud-arrow-up-fill", "flower1", "camera-reels-fill"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "nav-link-selected": {
                "background-color": "#7ff00e",  # Background color of the selected item
                "color": "black",
            },
            "nav-link": {
                "background-color": "#cafa9b",  # Background color of unselected items
                "color": "black",  # Text color of unselected items
            },
        },
    )

    # Render the selected page
    if selected_page == "Home":
        home_page()
    elif selected_page == "Predictions":
        #clear session state
        prediction_page()
    elif selected_page == "Plants Data":
        plants_page()
    elif selected_page == "Recommendations":
        about_us_page()
