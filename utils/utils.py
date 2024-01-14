# import validators
import re
import numpy as np
import matplotlib.pyplot as plt

def is_valid_http(http_payload):
    # return validators.url(http_payload)
    pattern = "^https:\/\/[0-9A-z.]+.[0-9A-z.]+.[a-z]+$"
    result = re.match(pattern, http_payload)
    return True if result else False

def move_pixels_to_center(image):
    for i in range(2):
        non_empty = np.nonzero(np.any(image, axis=1-i))[0]
        if len(non_empty) > 0:
            first, last = non_empty.min(), non_empty.max()
            shift = (image.shape[i] - first - last) // 2
            image = np.roll(image, shift=shift, axis=i)
    return image

def move_pixels_to_bottom(image):
    for i in range(2):
        non_empty = np.nonzero(np.any(image, axis=1-i))[0]
        if len(non_empty) > 0:
            first, last = non_empty.min(), non_empty.max()
            shift = (image.shape[i] - first - last) // -15
            image = np.roll(image, shift=shift, axis=i)
    return image

def visualize_payload(payload):
    plt.imshow(payload)
    plt.axis('off')
    plt.show()