
# Autonomous Vehicle Navigation System (Enhanced)

## Overview
This project implements an autonomous vehicle navigation system using Python, Computer Vision, and Embedded Systems. The system integrates sensor data, processes it in real-time using RTOS concepts, and uses control algorithms to navigate the vehicle. This enhanced version includes advanced computer vision techniques, real hardware integration, detailed logging, and extended RTOS features.

## Project Structure
- `sensor_integration.py`: Integrates and preprocesses sensor data from GPS, LiDAR, and Camera. Now includes examples of interfacing with real hardware.
- `rtos_simulation.py`: Simulates RTOS task scheduling for sensor data processing, with additional features like interrupt handling.
- `computer_vision.py`: Processes camera data using advanced Computer Vision techniques like object detection.
- `logging_example.py`: Demonstrates enhanced logging and debugging in Python scripts.

## How to Execute the Project

1. **Clone the Repository**
   First, clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/autonomous-vehicle-navigation.git
   cd autonomous-vehicle-navigation
   ```

2. **Download Sensor Data Files**
   Download the sensor data files and place them in the project directory:
   - Download GPS Data (gps_data.csv)
   - Download LiDAR Data (lidar_data.csv)
   - Download Camera Data (camera_data.txt)

3. **Install Dependencies**
   Ensure you have Python installed, along with the necessary packages:
   ```bash
   pip install numpy opencv-python pyserial
   ```

4. **Sensor Integration**
   Run `sensor_integration.py` to generate and preprocess synthetic sensor data or interface with real hardware:
   ```bash
   python sensor_integration.py
   ```

5. **RTOS Simulation**
   Run `rtos_simulation.py` to simulate task scheduling, mimicking the behavior of an RTOS:
   ```bash
   python rtos_simulation.py
   ```

6. **Computer Vision Processing**
   Run `computer_vision.py` to process camera images, applying techniques like object detection:
   ```bash
   python computer_vision.py
   ```

7. **Logging Example**
   Run `logging_example.py` to see enhanced logging in action:
   ```bash
   python logging_example.py
   ```

## Potential Additions
If you want to expand the project or tailor it to more specific requirements, here are a few things you could consider adding:
- **Advanced Computer Vision Techniques**: Integrate more sophisticated image processing or object detection algorithms.
- **Integration with Real Hardware**: Connect to actual sensors or simulate more complex data.
- **Logging and Debugging**: Include more extensive logging and debugging information.
- **Extended RTOS Features**: If using actual RTOS, integrate real-time scheduling and interrupt handling.

## Contributing
Feel free to submit a pull request or open an issue if you have suggestions or improvements. Contributions are welcome!

## License
This project is licensed under the MIT License.

## Contact
For questions or collaboration, please contact [Your Name](mailto:your-email@example.com).
