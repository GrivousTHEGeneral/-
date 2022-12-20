import numpy as np
import os
import time

#Read input data from command line
input_data = np.array(input().split(' '))
ip_addres, port_number, mqtt_name, speed_linear, speed_angel, robot_path_txt = input_data[1:]

port_number = int(port_number)
speed_linear = float(speed_linear)
speed_angel = float(speed_angel)

with open(robot_path_txt) as f: #Open txt file with data
    robot_path = f.readlines()
    robot_path = np.array([line.rstrip().split(' ') for line in robot_path], dtype=float)

def Distanse(point1, point2) -> float: #Calculate Euclidean metric
    point1, point2 = np.array(point1, dtype=float), np.array(point2, dtype=float)
    return np.linalg.norm(point1 - point2)

def Angel(vector1, vector2) -> float: #Calculate angel in Euclidean space
    vector1, vector2 = np.array(vector1, dtype=float), np.array(vector2, dtype=float)
    norm_v1 = np.linalg.norm(vector1)
    norm_v2 = np.linalg.norm(vector2)
    if norm_v2 == 0.0 or norm_v1 == 0.0:
        return 0.0
    else:
        return np.arccos(np.clip(np.dot(vector1, vector2) / (norm_v1 * norm_v2), -1.0, 1))

#Start parameters
start_point = robot_path[0]
v1 = start_point
total_time = 0
total_dist = 0

#The beginning of the path
os.system(f"mosquitto_pub -h {ip_addres} -p {port_number} -t {mqtt_name} -m 'Start\n'")
for point in robot_path[1:]:

    #Calc dist of path and time-travel
    dist = Distanse(start_point, point)
    time_linear = dist / speed_linear

    #Calc angle of rotation and time of rotation
    v2 = point - start_point
    angle_rot = Angel(v1, v2)
    time_rot = angle_rot / speed_angel

    #Calc total dist of path and total time-travel
    total_time += time_linear + time_rot
    total_dist += dist

    #Publish step to MQTT broker
    time.sleep(time_rot)
    os.system(f"mosquitto_pub -h {ip_addres} -p {port_number} -t {mqtt_name} -m 'Angle of rotation: {round(angle_rot, 2)}; Time of rotation: {round(time_rot, 2)}.'")
    time.sleep(time_linear)
    os.system(f"mosquitto_pub -h {ip_addres} -p {port_number} -t {mqtt_name} -m 'Distanse: {round(dist, 2)}; Travel time: {round(time_linear, 2)}.\n'")

    start_point = point
    v1 = v2

os.system(f"mosquitto_pub -h {ip_addres} -p {port_number} -t {mqtt_name} -m '\n\nEnd. Total distanse: {round(total_dist, 2)}; Total time: {round(total_time , 2)}.\n'")