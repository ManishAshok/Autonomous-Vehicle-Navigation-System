
import numpy as np
import pandas as pd

def generate_gps_data(num_points):
    latitude = np.random.uniform(-90, 90, num_points)
    longitude = np.random.uniform(-180, 180, num_points)
    altitude = np.random.uniform(0, 1000, num_points)
    return pd.DataFrame({'Latitude': latitude, 'Longitude': longitude, 'Altitude': altitude})

def generate_lidar_data(num_points):
    distances = np.random.uniform(1, 100, num_points)
    angles = np.linspace(0, 360, num_points)
    return pd.DataFrame({'Distance': distances, 'Angle': angles})

def generate_camera_data(image_size):
    return np.random.randint(0, 256, size=(image_size, image_size))

gps_data = generate_gps_data(100)
lidar_data = generate_lidar_data(360)
camera_data = generate_camera_data(64)

gps_data.to_csv('gps_data.csv', index=False)
lidar_data.to_csv('lidar_data.csv', index=False)
np.savetxt('camera_data.txt', camera_data, fmt='%d')
