
import cv2
import numpy as np

def process_camera_image(image_file):
    image = np.loadtxt(image_file, dtype=np.uint8)
    image = cv2.resize(image, (128, 128))  # Resize for processing

    # Apply edge detection
    edges = cv2.Canny(image, 50, 150)

    # Load Haar Cascade for object detection (e.g., cars)
    car_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_car.xml')

    # Detect objects
    cars = car_cascade.detectMultiScale(edges, 1.1, 1)

    # Draw bounding boxes around detected objects
    for (x, y, w, h) in cars:
        cv2.rectangle(edges, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Save the processed image with detections
    cv2.imwrite('processed_image_with_detections.png', edges)

    return edges

# Process the synthetic camera data
processed_image = process_camera_image('camera_data.txt')
