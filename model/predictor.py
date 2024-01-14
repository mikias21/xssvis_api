import os
from tensorflow.keras.models import load_model

def classify(payload):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_directory, "xssvis_classifier.h5")
    classifier = load_model("model/xssvis_classifier.h5", compile=False)
    predictions = classifier.predict(payload)
    return predictions