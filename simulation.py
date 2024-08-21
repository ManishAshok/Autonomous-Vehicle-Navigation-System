
import numpy as np

def navigate_to_waypoint(current_position, target_position):
    direction = np.arctan2(target_position[1] - current_position[1], target_position[0] - current_position[0])
    distance = np.sqrt((target_position[0] - current_position[0])**2 + (target_position[1] - current_position[1])**2)
    print(f"Direction to waypoint: {np.degrees(direction)} degrees")
    print(f"Distance to waypoint: {distance} meters")
    return direction, distance

def simulate_vehicle():
    current_position = np.array([0, 0])
    waypoints = [np.array([10, 0]), np.array([10, 10]), np.array([0, 10]), np.array([0, 0])]

    for waypoint in waypoints:
        direction, distance = navigate_to_waypoint(current_position, waypoint)
        current_position = waypoint  # Simulate moving to the waypoint
        print(f"Vehicle reached waypoint at {current_position}\n")

simulate_vehicle()
