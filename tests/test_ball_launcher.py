import unittest
from ball_launcher import BallLauncher

class TestBallLauncher(unittest.TestCase):
    def setUp(self):
        self.ball_launcher = BallLauncher()

    def test_calculate_arm_mass(self):
        expected_mass = 2700 * 0.2 * 0.015 * 0.015
        self.assertAlmostEqual(self.ball_launcher.calculate_arm_mass(), expected_mass, places=5)

    def test_calculate_launch_velocity(self):
        motor_torque = 1.5
        motor_speed = 15
        launch_velocity = self.ball_launcher.calculate_launch_velocity(motor_torque, motor_speed)
        self.assertGreater(launch_velocity, 0)
        self.assertLessEqual(launch_velocity, self.ball_launcher.max_speed * self.ball_launcher.arm_length)

if __name__ == '__main__':
    unittest.main()
