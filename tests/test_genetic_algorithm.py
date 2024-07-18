import unittest
from ball_launcher import BallLauncher
from simulator import Simulator
from genetic_algorithm import GeneticAlgorithm

class TestGeneticAlgorithm(unittest.TestCase):
    def setUp(self):
        self.ball_launcher = BallLauncher()
        self.simulator = Simulator(self.ball_launcher)
        self.ga = GeneticAlgorithm(self.simulator)

    def test_initialize_population(self):
        population = self.ga.initialize_population()
        self.assertEqual(len(population), self.ga.population_size)
        for individual in population:
            self.assertIn('motor_torque', individual)
            self.assertIn('motor_speed', individual)
            self.assertIn('launch_angle', individual)

    def test_evaluate_fitness(self):
        individual = {
            'motor_torque': 1.5,
            'motor_speed': 15,
            'launch_angle': 45
        }
        fitness = self.ga.evaluate_fitness(individual)
        self.assertGreater(fitness, 0)

    def test_select_parents(self):
        parents = self.ga.select_parents()
        self.assertEqual(len(parents), 2)

    def test_crossover(self):
        parent1 = {
            'motor_torque': 1.5,
            'motor_speed': 15,
            'launch_angle': 45
        }
        parent2 = {
            'motor_torque': 1.0,
            'motor_speed': 10,
            'launch_angle': 30
        }
        child = self.ga.crossover(parent1, parent2)
        self.assertIn('motor_torque', child)
        self.assertIn('motor_speed', child)
        self.assertIn('launch_angle', child)

    def test_mutate(self):
        individual = {
            'motor_torque': 1.5,
            'motor_speed': 15,
            'launch_angle': 45
        }
        mutated_individual = self.ga.mutate(individual)
        self.assertIn('motor_torque', mutated_individual)
        self.assertIn('motor_speed', mutated_individual)
        self.assertIn('launch_angle', mutated_individual)

    def test_run(self):
        best_individual = self.ga.run()
        self.assertIn('motor_torque', best_individual)
        self.assertIn('motor_speed', best_individual)
        self.assertIn('launch_angle', best_individual)

if __name__ == '__main__':
    unittest.main()
