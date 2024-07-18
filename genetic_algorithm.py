import random

class GeneticAlgorithm:
    def __init__(self, simulator, population_size=50, generations=100, mutation_rate=0.01):
        self.simulator = simulator
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.population = self.initialize_population()

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            individual = {
                'motor_torque': random.uniform(0, self.simulator.ball_launcher.max_torque),
                'motor_speed': random.uniform(0, self.simulator.ball_launcher.max_speed),
                'launch_angle': random.uniform(0, 90)
            }
            population.append(individual)
        return population

    def evaluate_fitness(self, individual):
        distance = self.simulator.simulate(individual['motor_torque'], individual['motor_speed'], individual['launch_angle'])
        return distance

    def select_parents(self):
        sorted_population = sorted(self.population, key=self.evaluate_fitness, reverse=True)
        return sorted_population[:2]

    def crossover(self, parent1, parent2):
        child = {
            'motor_torque': (parent1['motor_torque'] + parent2['motor_torque']) / 2,
            'motor_speed': (parent1['motor_speed'] + parent2['motor_speed']) / 2,
            'launch_angle': (parent1['launch_angle'] + parent2['launch_angle']) / 2
        }
        return child

    def mutate(self, individual):
        if random.random() < self.mutation_rate:
            individual['motor_torque'] = random.uniform(0, self.simulator.ball_launcher.max_torque)
        if random.random() < self.mutation_rate:
            individual['motor_speed'] = random.uniform(0, self.simulator.ball_launcher.max_speed)
        if random.random() < self.mutation_rate:
            individual['launch_angle'] = random.uniform(0, 90)
        return individual

    def run(self):
        for generation in range(self.generations):
            new_population = []
            for _ in range(self.population_size):
                parent1, parent2 = self.select_parents()
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)
            self.population = new_population
            best_individual = max(self.population, key=self.evaluate_fitness)
            print(f"Generation {generation}: Best Distance = {self.evaluate_fitness(best_individual):.2f} meters")
        return best_individual
