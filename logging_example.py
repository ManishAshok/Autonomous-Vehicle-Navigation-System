
import logging

# Configure logging
logging.basicConfig(filename='vehicle_navigation.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def log_example():
    logging.info("Starting the vehicle navigation system.")
    try:
        # Simulate a process
        result = 10 / 0
    except ZeroDivisionError as e:
        logging.error("An error occurred: %s", e)
    logging.info("Vehicle navigation system finished.")

log_example()
