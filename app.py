 
from flask import Flask, render_template, request, url_for
import numpy as np
from tensorflow.keras import models
import os

app = Flask(__name__, static_url_path='/images', static_folder='images')

# Define the penguin classes
penguin_classes = ['Adelie', 'Gentoo', 'Chinstrap']

# Load the saved model
model_file_name = os.path.join('models', 'penguin-classifier.h5')
model = models.load_model(model_file_name)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify_penguin', methods=['POST'])
def classify_penguin():
    # Get the features from the request
    features = [float(request.form['CulmenLength']), float(request.form['CulmenDepth']),
                float(request.form['FlipperLength']), float(request.form['BodyMass'])]
    x_new = np.array([features])

    # Use the model to predict the class
    class_probabilities = model.predict(x_new)
    predictions = np.argmax(class_probabilities, axis=1)

    # Get the corresponding class label
    predicted_class = penguin_classes[predictions[0]]
    image_url = url_for('static', filename=f'{predicted_class.lower()}.jpg')

    return render_template('show_image.html', image_url=image_url, species=predicted_class)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
