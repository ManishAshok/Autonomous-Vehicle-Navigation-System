
import time
import threading

def gps_task():
    while True:
        print("Processing GPS data...")
        time.sleep(1)  # Simulate a 1 Hz GPS update rate

def lidar_task():
    while True:
        print("Processing LiDAR data...")
        time.sleep(0.1)  # Simulate a 10 Hz LiDAR update rate

def camera_task():
    while True:
        print("Processing Camera data...")
        time.sleep(0.05)  # Simulate a 20 Hz Camera frame rate

threading.Thread(target=gps_task).start()
threading.Thread(target=lidar_task).start()
threading.Thread(target=camera_task).start()
