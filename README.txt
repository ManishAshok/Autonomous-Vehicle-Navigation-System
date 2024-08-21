
# Autonomous Vehicle Navigation System

## Overview
This project implements an autonomous vehicle navigation system using Python, Computer Vision, and Embedded Systems. The system integrates sensor data, processes it in real-time using RTOS concepts, and uses control algorithms to navigate the vehicle.

## Project Structure
- `sensor_integration.py`: Integrates and preprocesses sensor data.
- `rtos_simulation.py`: Simulates RTOS task scheduling for sensor data processing.
- `computer_vision.py`: Processes camera data using Computer Vision techniques.
- `control_algorithms.py`: Implements navigation and control algorithms.
- `simulation.py`: Simulates the vehicle's navigation and control system.

## How to Run the Project
1. **Sensor Integration**:
   Run `sensor_integration.py` to generate and preprocess synthetic sensor data.
   ```bash
   python sensor_integration.py
   ```

2. **RTOS Simulation**:
   Run `rtos_simulation.py` to simulate task scheduling.
   ```bash
   python rtos_simulation.py
   ```

3. **Computer Vision Processing**:
   Run `computer_vision.py` to process camera images.
   ```bash
   python computer_vision.py
   ```

4. **Navigation and Control**:
   Run `control_algorithms.py` to execute navigation algorithms.
   ```bash
   python control_algorithms.py
   ```

5. **System Simulation**:
   Run `simulation.py` to simulate the vehicle's response to navigation commands.
   ```bash
   python simulation.py
   ```

## Requirements
- Python 3.x
- NumPy
- OpenCV
