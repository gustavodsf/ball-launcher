import unittest
from ball_launcher import BallLauncher
from simulator import Simulator

class TestSimulator(unittest.TestCase):
    def setUp(self):
        self.ball_launcher = BallLauncher()
        self.simulator = Simulator(self.ball_launcher)

    def test_calculate_launch_distance(self):
        launch_velocity = 10
        launch_angle = 45
        distance = self.simulator.calculate_launch_distance(launch_velocity, launch_angle)
        self.assertGreater(distance, 0)

    def test_simulate(self):
        motor_torque = 1.5
        motor_speed = 15
        launch_angle = 45
        distance = self.simulator.simulate(motor_torque, motor_speed, launch_angle)
        self.assertGreater(distance, 0)

if __name__ == '__main__':
    unittest.main()
