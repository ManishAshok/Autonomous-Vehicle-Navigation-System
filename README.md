<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Autonomous Vehicle Navigation System</h1>

<h2>Overview</h2>
<p>This project implements an autonomous vehicle navigation system using Python, Computer Vision, and Embedded Systems. The system integrates sensor data, processes it in real-time using RTOS concepts, and uses control algorithms to navigate the vehicle. This project demonstrates the potential of autonomous navigation, which is crucial for self-driving cars, robotics, and other autonomous systems.</p>

<h2>Project Structure</h2>
<ul>
    <li><strong>sensor_integration.py</strong>: Integrates and preprocesses sensor data from GPS, LiDAR, and Camera.</li>
    <li><strong>rtos_simulation.py</strong>: Simulates RTOS task scheduling for sensor data processing.</li>
    <li><strong>computer_vision.py</strong>: Processes camera data using Computer Vision techniques to identify obstacles or lane markings.</li>
    <li><strong>control_algorithms.py</strong>: Implements navigation and control algorithms, such as waypoint navigation and obstacle avoidance.</li>
    <li><strong>simulation.py</strong>: Simulates the vehicle's navigation and control system, demonstrating how the vehicle responds to sensor inputs and control commands.</li>
</ul>

<h2>How to Execute the Project</h2>

<h3>1. Clone the Repository</h3>
<p>First, clone this repository to your local machine:</p>
<pre><code>git clone https://github.com/ManishAshok/autonomous-vehicle-navigation.git
cd autonomous-vehicle-navigation</code></pre>
<h3>2. Download Sensor Data Files</h3>

<p>Download the sensor data files and place them in the project directory:</p>
<ul>
    <li><a href="data/gps_data.csv">Download GPS Data (gps_data.csv)</a></li>
    <li><a href="data/lidar_data.csv">Download LiDAR Data (lidar_data.csv)</a></li>
    <li><a href="mnt/data/camera_data.txt">Download Camera Data (camera_data.txt)</a></li>
</ul>

<h3>Install Dependencies</h3>
<p>Ensure you have Python installed, along with the necessary packages:</p>
<pre><code>pip install numpy opencv-python</code></pre>

<h3>3. Sensor Integration</h3>
<p>Run <code>sensor_integration.py</code> to generate and preprocess synthetic sensor data:</p>
<pre><code>python sensor_integration.py</code></pre>

<h3>4. RTOS Simulation</h3>
<p>Run <code>rtos_simulation.py</code> to simulate task scheduling, mimicking the behavior of an RTOS:</p>
<pre><code>python rtos_simulation.py</code></pre>

<h3>5. Computer Vision Processing</h3>
<p>Run <code>computer_vision.py</code> to process camera images, applying techniques like edge detection:</p>
<pre><code>python computer_vision.py</code></pre>

<h3>6. Navigation and Control</h3>
<p>Run <code>control_algorithms.py</code> to execute navigation algorithms such as waypoint navigation:</p>
<pre><code>python control_algorithms.py</code></pre>

<h3>7. System Simulation</h3>
<p>Finally, run <code>simulation.py</code> to simulate the vehicle's response to navigation commands:</p>
<pre><code>python simulation.py</code></pre>

<h2>Project Potential</h2>
<p>The Autonomous Vehicle Navigation System developed in this project showcases the foundational components needed for self-driving technology. By integrating real-time sensor data processing with navigation algorithms, the system can be extended and enhanced to support full-scale autonomous vehicles. Potential applications include:</p>
<ul>
    <li><strong>Self-Driving Cars:</strong> Core navigation algorithms and sensor fusion techniques are applicable to real-world autonomous vehicles.</li>
    <li><strong>Robotics:</strong> The control system can be adapted for autonomous drones, robots, and other automated systems.</li>
    <li><strong>Safety and Precision:</strong> RTOS integration ensures that the system operates with high precision and safety in time-critical environments.</li>
</ul>

<h2>Contributing</h2>
<p>Feel free to submit a pull request or open an issue if you have suggestions or improvements. Contributions are welcome!</p>

<h2>License</h2>
<p>This project is licensed under the MIT License.</p>

</body>
</html>
