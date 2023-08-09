 
from flask import Flask, render_template, request, url_for
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os

app = Flask(__name__, static_url_path='/images', static_folder='images')

# Define the classes (adjust based on your model's classes)
classes = ['Jiraiya', 'Sakura', 'Sasuke']  # Replace with your class names

# Recreate the model architecture
base_model = ResNet50(weights=None, include_top=False)  # Set weights to None

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation='relu')(x)  # Removed regularization for simplicity
x = Dropout(0.6)(x)
predictions = Dense(3, activation='softmax')(x)  # Adjusted for 3 classes
model = Model(inputs=base_model.input, outputs=predictions)

# Load the saved weights
weights_file_name = os.path.join('models', 'model_weights_only.h5')
model.load_weights(weights_file_name)

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/classify_image', methods=['POST'])
def classify_image():
    # Get the image from the POST request
    uploaded_image = request.files['image']
    img = load_img(uploaded_image, target_size=(224, 224))  # Adjust target size based on your model's input size
    img_array = img_to_array(img) / 255.  # Ensure to rescale as you did during training
    img_array = np.expand_dims(img_array, axis=0)

    # Use the model to predict the class
    class_probabilities = model.predict(img_array)
    predictions = np.argmax(class_probabilities, axis=1)

    # Get the corresponding class label
    predicted_class = classes[predictions[0]]
    image_url = url_for('static', filename=f'{predicted_class.lower()}.jpg')

    return render_template('result.html', image_url=image_url, label=predicted_class)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
