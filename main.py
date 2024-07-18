from ball_launcher import BallLauncher
from genetic_algorithm import GeneticAlgorithm
from simulator import Simulator

# Example usage
# Example usage
if __name__ == "__main__":
    ball_launcher = BallLauncher()
    simulator = Simulator(ball_launcher)
    ga = GeneticAlgorithm(simulator)
    best_parameters = ga.run()
    print(f"Best parameters: {best_parameters}")