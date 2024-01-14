import os
import uuid
from fastapi import status
import matplotlib.pyplot as plt

# Local
from model.predictor import classify
from schemes.request import XssRequestModel
from utils.generators import get_processed_payload

def xss_detection_controller(http_req: XssRequestModel):
    payload = get_processed_payload(http_req.http_url, center=True)
    
    image_name = str(uuid.uuid4()) + '.png'
    generated_image = f"generated_images/{image_name}"

    os.makedirs("generated_images", exist_ok=True)

    # Generate image
    plt.imshow(payload)
    plt.axis('off')
    plt.savefig(generated_image)
    plt.close()

    # predict
    payload = payload.reshape(-1, 32, 32, 3)
    classification = classify(payload)
    print(classification)

    return image_name