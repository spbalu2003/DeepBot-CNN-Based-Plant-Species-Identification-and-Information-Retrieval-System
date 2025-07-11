import streamlit as st
import requests
YOUTUBE_API_KEY = "AIzaSyDYEeSTrT7pPpVzpmaJ491gxogVxfWwpvM"

def fetch_youtube_videos(query, max_results=6):
    url = f"https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'key': YOUTUBE_API_KEY,
        'maxResults': max_results
    }
    response = requests.get(url, params=params)
    videos = []
    if response.status_code == 200:
        data = response.json()
        for item in data['items']:
            video_id = item['id']['videoId']
            video_title = item['snippet']['title']
            videos.append({'video_id': video_id, 'title': video_title})
    return videos

def about_us_page():
    # About Us page description
    st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://static.vecteezy.com/system/resources/thumbnails/029/109/949/small_2x/wild-pristine-evergreen-forest-ai-generated-photo.jpg');
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
    with st.form('About Us'):
        # Contact Us Form
        st.subheader("Plant Growth Guide")
        class_labels = ['African Violet', 'Aloe Vera',
            'Anthurium',
            'Areca Palm',
            'Asparagus Fern',
            'Begonia', 'Bird of Paradise',
            'Birds Nest Fern',
            'Boston Fern', 'Calathea',
            'Cast Iron Plant',
            'Chinese Money Plant',
            'Chinese evergreen',
            'Christmas Cactus', 'Chrysanthemum',
            'Ctenanthe', 'Daffodils', 'Dracaena',
            'Dumb Cane', 'Elephant Ear',
            'English Ivy', 'Hyacinth',
            'Iron Cross begonia',
            'Jade plant', 'Kalanchoe',
            'Lilium',
            'Lily of the valley',
            'Money Tree',
            'Monstera Deliciosa', 'Orchid',
            'Parlor Palm', 'Peace lily',
            'Poinsettia',
            'Polka Dot Plan',
            'Ponytail Palm', 'Pothos',
            'Prayer',
            'Rattlesnake',
            'Rubber', 'Sago Palm',
            'Schefflera', 'Snake Plant', 'Tradescantia', 'Tulip',
            'Venus Flytrap', 'Yucca', 'Zamioculcas zamiifolia']
        #make slecetion
        col1, col2 = st.columns(2)
        plant = col1.selectbox('Select Plant', class_labels, key='plant')
        query = f"{plant} plant care"
        if st.form_submit_button('Search Videos',type='primary'):
            videos = fetch_youtube_videos(query)

            # Display videos in rows of 3
            for i in range(0, len(videos), 2):
                cols = st.columns(2)  # Create 3 columns
                for j, video in enumerate(videos[i:i+2]):  # Iterate over videos for the current row
                    with cols[j]:
                        st.video(f"https://www.youtube.com/watch?v={video['video_id']}")
    
