
import numpy as np

def navigate_to_waypoint(current_position, target_position):
    direction = np.arctan2(target_position[1] - current_position[1], target_position[0] - current_position[0])
    distance = np.sqrt((target_position[0] - current_position[0])**2 + (target_position[1] - current_position[1])**2)
    print(f"Direction to waypoint: {np.degrees(direction)} degrees")
    print(f"Distance to waypoint: {distance} meters")
    return direction, distance

current_position = (0, 0)
target_position = (10, 10)
navigate_to_waypoint(current_position, target_position)
