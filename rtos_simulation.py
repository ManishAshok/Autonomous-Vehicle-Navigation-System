
import threading
import time
import logging

# Configure logging for RTOS simulation
logging.basicConfig(filename='rtos_simulation.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def gps_task():
    while True:
        logging.info("Processing GPS data...")
        time.sleep(1)  # Simulate a 1 Hz GPS update rate

def lidar_task():
    while True:
        logging.info("Processing LiDAR data...")
        time.sleep(0.1)  # Simulate a 10 Hz LiDAR update rate

def camera_task():
    while True:
        logging.info("Processing Camera data...")
        time.sleep(0.05)  # Simulate a 20 Hz Camera frame rate

def emergency_brake_interrupt():
    logging.info("Emergency brake activated!")
    time.sleep(0.01)  # Simulate fast response interrupt

# Create and start threads for each task
threads = [
    threading.Thread(target=gps_task),
    threading.Thread(target=lidar_task),
    threading.Thread(target=camera_task),
]

for thread in threads:
    thread.start()

# Simulate an emergency brake interrupt after 5 seconds
time.sleep(5)
emergency_brake_interrupt()
