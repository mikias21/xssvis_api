import numpy as np
from urllib.parse import urlparse

# Local
from constants.general import General
from utils.utils import is_valid_http
from utils.utils import move_pixels_to_bottom, move_pixels_to_center, visualize_payload

def parse_http_request(payload):
    parsed_payload = urlparse(payload)
    path = parsed_payload.path 
    query = parsed_payload.query 
    if query:
        if '=' in query:
            query = query.split('=', 1)
            return query[-1]
        elif '&' in query:
            query = query.split('&', 1)
            return query[-1]
    elif path:
        return path 
    else:
            return payload

def get_ascii(payload):
    ascii_vector = []
    if payload is not None:
        if is_valid_http(payload):
            parsed_payload = parse_http_request(payload)
            if parsed_payload:
                for char in parsed_payload:
                    ascii_vector.append(ord(char))
        else:
            for char in payload:
                ascii_vector.append(ord(char))
    
    need_padding = True 
    while need_padding:
        if len(ascii_vector) < General.PAYLOAD_LENGTH.value:
            ascii_vector.append(0)
        else:
            need_padding = False 
        
    return ascii_vector 

def convert_payload_to_pixel(payload_ascii, center=False, bottom=False):
    initial_image = np.zeros((32, 32, 3))
    initial_image += initial_image + np.reshape(payload_ascii, (32, 32, 3))
    if center:
        return move_pixels_to_center(initial_image)
    elif bottom:
        return move_pixels_to_bottom(initial_image)
    else:
        return initial_image

def get_processed_payload(payload, visualize=False, center=False, bottom=False):
    payload = convert_payload_to_pixel(get_ascii(payload), center, bottom)
    payload /= 255.0
    if visualize:
        visualize_payload(payload)
    return payload 