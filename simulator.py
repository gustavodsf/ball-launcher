import math

class Simulator:
    def __init__(self, ball_launcher):
        self.ball_launcher = ball_launcher

    def calculate_launch_distance(self, launch_velocity, launch_angle):
        # Convert launch angle to radians
        launch_angle_rad = math.radians(launch_angle)
        
        # Calculate the horizontal and vertical components of the velocity
        v_x = launch_velocity * math.cos(launch_angle_rad)
        v_y = launch_velocity * math.sin(launch_angle_rad)
        
        # Calculate the time of flight (t = 2 * v_y / g)
        g = 9.81  # acceleration due to gravity in m/s^2
        time_of_flight = (2 * v_y) / g
        
        # Calculate the horizontal distance (d = v_x * t)
        launch_distance = v_x * time_of_flight
        
        return launch_distance

    def simulate(self, motor_torque, motor_speed, launch_angle):
        launch_velocity = self.ball_launcher.calculate_launch_velocity(motor_torque, motor_speed)
        launch_distance = self.calculate_launch_distance(launch_velocity, launch_angle)
        return launch_distance
