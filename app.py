from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
from keras.models import model_from_json
import numpy as np
import base64

app = Flask(__name__)
CORS(app)

# Load the model
json_file = open("stressdetector.json", "r")
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights("stressdetectorV1.h5")

# Load the Haar Cascade file
haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)

# Define the labels
labels = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprise'}

# Function to extract features from the image
def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1, 48, 48, 1)
    return feature / 255.0

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    img_data = base64.b64decode(data['image'])
    nparr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    predictions = []

    for (x, y, w, h) in faces:
        face = gray[y:y + h, x:x + w]
        face = cv2.resize(face, (48, 48))
        img = extract_features(face)
        pred = model.predict(img)
        prediction_label = labels[pred.argmax()]

        if prediction_label in ['angry', 'disgust', 'fear', 'sad']:
            state = 'stressed'
        else:
            state = 'not stressed'

        predictions.append({
            'label': prediction_label,
            'state': state,
            'box': [int(x), int(y), int(w), int(h)]
        })

    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
