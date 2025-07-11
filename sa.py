import tensorflow as tf
import keras.backend as K

# Define the custom Lambda function
def custom_lambda(x):
    return K.exp(x)  # Example function, replace with your actual Lambda function

# Load model with custom Lambda function
model = tf.keras.models.load_model("plant_species_model.keras", custom_objects={'custom_lambda': custom_lambda})

# Define the image size (should match the input size used during training)
IMG_SIZE = 224

# Function to preprocess the image
def preprocess_image(image_path, img_size=IMG_SIZE):
    """
    Takes an image file path, reads and preprocesses the image.
    """
    # Read the image file
    image = tf.io.read_file(image_path)
    # Decode the image to a tensor
    image = tf.image.decode_jpeg(image, channels=3)
    # Resize the image
    image = tf.image.resize(image, [img_size, img_size])
    # Normalize the image to [0, 1]
    image = image / 255.0
    # Add a batch dimension
    image = tf.expand_dims(image, axis=0)
    return image

# Function to make predictions
def predict_image_class(image_path, model, class_names):
    """
    Takes an image path, preprocesses it, and makes a prediction using the model.
    """
    # Preprocess the image
    image = preprocess_image(image_path)
    # Make prediction
    predictions = model.predict(image)
    # Get the predicted class index
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    # Get the predicted class name
    predicted_class_name = class_names[predicted_class_index]
    # Get the confidence score
    confidence = np.max(predictions)
    return predicted_class_name, confidence

# Example usage
if __name__ == "__main__":
    # Define the path to the image you want to predict
    image_path = "uploads/2.jpg"  # Replace with your image path

    # Define the class names (replace with your actual class names)
    class_names = ['African Violet (Saintpaulia ionantha)', 'Aloe Vera',
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

    # Make prediction
    predicted_class, confidence = predict_image_class(image_path, model, class_names)
    print(f"Predicted Class: {predicted_class}, Confidence: {confidence:.2f}")