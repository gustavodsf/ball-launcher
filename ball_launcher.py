import math

class BallLauncher:
    def __init__(self, arm_length=0.2, ball_diameter=0.015, max_torque=2, max_speed=20):
        self.arm_length = arm_length  # in meters
        self.ball_diameter = ball_diameter  # in meters
        self.max_torque = max_torque  # in Newton-meters
        self.max_speed = max_speed  # in radians per second

    def calculate_launch_velocity(self, motor_torque, motor_speed):
        # Ensure motor parameters are within limits
        motor_torque = min(motor_torque, self.max_torque)
        motor_speed = min(motor_speed, self.max_speed)
        
        # Calculate the angular acceleration (alpha = torque / inertia)
        # Inertia (I) for a rod rotating about one end: I = (1/3) * mass * length^2
        arm_mass = self.calculate_arm_mass()
        inertia = (1/3) * arm_mass * (self.arm_length ** 2)
        angular_acceleration = motor_torque / inertia
        
        # Calculate the time to reach max speed (omega = alpha * t)
        time_to_max_speed = motor_speed / angular_acceleration
        
        # Calculate the linear velocity at the end of the arm (v = omega * r)
        launch_velocity = motor_speed * self.arm_length
        
        return launch_velocity

    def calculate_arm_mass(self):
        # Density of 6061 aluminum alloy: 2700 kg/m^3
        density = 2700
        volume = self.arm_length * 0.015 * 0.015  # length * width * height (assuming width and height are 15mm)
        mass = density * volume
        return mass
