import numpy as np
from tensorflow.keras.models import load_model

def classify(payload):
    classifier = load_model("model/xssvis_classifier.h5", compile=False)
    prediction = np.argmax(classifier.predict(payload))
    return prediction