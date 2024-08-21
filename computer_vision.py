
import cv2
import numpy as np

def process_camera_image(image_file):
    image = np.loadtxt(image_file, dtype=np.uint8)
    image = cv2.resize(image, (128, 128))  # Resize for processing
    edges = cv2.Canny(image, 50, 150)
    cv2.imwrite('processed_image.png', edges)
    return edges

processed_image = process_camera_image('camera_data.txt')
