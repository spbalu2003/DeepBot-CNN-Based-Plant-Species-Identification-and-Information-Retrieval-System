import streamlit as st
import os
import pandas as pd
import numpy as np
import tensorflow_hub as hub
from tensorflow.keras.models import load_model
from keras.preprocessing import image
from tensorflow.keras.utils import load_img, img_to_array

# Model path
MODEL_PATH = r"model/20250217-1901-model_main.h5"
# Load model with the custom KerasLayer
model = load_model(MODEL_PATH, custom_objects={'KerasLayer': hub.KerasLayer})

# Define your class labels
class_labels = ['African Violet (Saintpaulia ionantha)', 'Aloe Vera',
       'Anthurium (Anthurium andraeanum)',
       'Areca Palm (Dypsis lutescens)',
       'Asparagus Fern (Asparagus setaceus)', 'Background_without_leaves',
       'Begonia (Begonia spp.)', 'Bird of Paradise (Strelitzia reginae)',
       'Birds Nest Fern (Asplenium nidus)',
       'Boston Fern (Nephrolepis exaltata)', 'Calathea',
       'Cast Iron Plant (Aspidistra elatior)',
       'Chinese Money Plant (Pilea peperomioides)',
       'Chinese evergreen (Aglaonema)',
       'Christmas Cactus (Schlumbergera bridgesii)', 'Chrysanthemum',
       'Ctenanthe', 'Daffodils (Narcissus spp.)', 'Dracaena',
       'Dumb Cane (Dieffenbachia spp.)', 'Elephant Ear (Alocasia spp.)',
       'English Ivy (Hedera helix)', 'Hyacinth (Hyacinthus orientalis)',
       'Iron Cross begonia (Begonia masoniana)',
       'Jade plant (Crassula ovata)', 'Kalanchoe',
       'Lilium (Hemerocallis)',
       'Lily of the valley (Convallaria majalis)',
       'Money Tree (Pachira aquatica)',
       'Monstera Deliciosa (Monstera deliciosa)', 'Orchid',
       'Parlor Palm (Chamaedorea elegans)', 'Peace lily',
       'Poinsettia (Euphorbia pulcherrima)',
       'Polka Dot Plant (Hypoestes phyllostachya)',
       'Ponytail Palm (Beaucarnea recurvata)', 'Pothos (Ivy arum)',
       'Prayer Plant (Maranta leuconeura)',
       'Rattlesnake Plant (Calathea lancifolia)',
       'Rubber Plant (Ficus elastica)', 'Sago Palm (Cycas revoluta)',
       'Schefflera', 'Snake plant (Sanseviera)', 'Tradescantia', 'Tulip',
       'Venus Flytrap', 'Yucca', 'ZZ Plant (Zamioculcas zamiifolia)']

def model_predict(img_path, model):
    img = load_img(img_path, target_size=(224, 224))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0  # Assuming your model expects normalized input
    preds = model.predict(x)
    return preds

def custom_decode_predictions(preds, class_labels, top=1):
    results = []
    for pred in preds:
        top_indices = pred.argsort()[-top:][::-1]  # Get indices of top predictions
        top_labels = [(class_labels[i], pred[i]) for i in top_indices]
        results.append(top_labels)
    return results
def prediction_page():
    # Center the login form using Streamlit form layout
    st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://www.shutterstock.com/image-photo/green-leaves-philodendron-plant-nature-260nw-2477697533.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: rgba(255, 255, 255, 0.7);
            background-blend-mode: overlay; 

        }
        </style>
        """,
        unsafe_allow_html=True
    )
    col1, col2,col3 = st.columns([1, 3,1])
    uploaded_file = col2.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    try:
        if uploaded_file is not None:
            # Save uploaded file to a temporary directory
            img_path = os.path.join("uploads", uploaded_file.name)
            with open(img_path, "wb") as f:
                f.write(uploaded_file.getbuffer())        
            def disease_info_box(disease_name):
                return f"""
                    <div style="
                        background-color: rgba(255, 255, 255, 0.6);
                        padding: 100px;
                        border-radius: 10px;
                        text-align: center;
                        font-size: 50px;
                        font-weight: bold;
                        color: red;">
                        {disease_name}
                    </div>
                """
            def desc_info(disease_name):
                return f"""
                    <div style="
                        background-color: rgb(25, 230, 10);
                        padding: 10px;
                        border-radius: 50px;
                        text-align: center;
                        font-size: 20px;
                        color: black;
                        border: 2px solid black;">
                        {disease_name}
                    </div>
                """

            def usage_info(disease_name):
                return f"""
                    <div style="
                        background-color: rgba(123, 216, 237, 0.6);
                        padding: 10px;
                        border-radius: 10px;
                        text-align: center;
                        font-size: 20px;
                        color: black;">
                        {disease_name}
                    </div>
                """
            # Make prediction
            preds = model_predict(img_path, model)
            st.write(preds)
            #max class index
            max_index = np.argmax(preds[0])
            max_index = int(max_index)
            if max_index == 5:
                col1,col2,col3=st.columns([2,3,2])
                col2.image('https://cdni.iconscout.com/illustration/premium/thumb/no-data-found-illustration-download-in-svg-png-gif-file-formats--office-computer-digital-work-business-pack-illustrations-7265556.png',caption='No Plant Detected',use_column_width=True)
            else:
                pred_class = custom_decode_predictions(preds, class_labels, top=1)
                result = str(pred_class[0][0][0])
                df=pd.read_csv('info.csv')
                #based on index get the info
                #columns are Index	Name	Desc	Usage	Link    
                res=df.loc[df['Index']==max_index]
                #info
                col1,col2=st.columns([2,2])
                col1.image(img_path, caption='Uploaded Image', use_column_width=True)
                col2.markdown(disease_info_box(res.iloc[0,1]), unsafe_allow_html=True)
                st.markdown(desc_info(res.iloc[0,2]), unsafe_allow_html=True)
                st.write('')
                st.markdown(usage_info(res.iloc[0,3]), unsafe_allow_html=True)
    except Exception as e:
        pass