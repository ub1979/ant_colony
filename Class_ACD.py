# ==============================================================
# Importing the libraries
# ==============================================================
import random
from typing import List, Callable

# ==============================================================
# Making the class of ACO
# ==============================================================
"""
Initialize the Ant Colony Optimization algorithm.

:param num_ants: Number of ants in the colony
:param num_cities: Number of cities in the problem
:param distance_func: Function to calculate distance between two cities
:param alpha: Importance of pheromone
:param beta: Importance of heuristic information
:param evaporation_rate: Rate at which pheromone evaporates
:param q: Pheromone deposit factor
:param initial_pheromone: Initial pheromone level on all edges
"""
class AntColonyOptimization:
    def __init__(self, num_ants: int, num_cities: int,
                 distance_func: Callable, alpha: float = 1.0,
                 beta: float = 2.0, evaporation_rate: float = 0.5,
                 q: float = 100, initial_pheromone: float = 1.0):

        # ========================================
        # setting the value of num_ants
        self.num_ants = num_ants

        # ========================================
        # setting the value of num_cities
        self.num_cities = num_cities

        # ========================================
        # setting the distance_func
        self.distance_func = distance_func

        # ========================================
        # setting the value of alpha
        self.alpha = alpha

        # ========================================
        # setting the value of beta
        self.beta = beta

        # ========================================
        # setting the value of evaporation_rate
        self.evaporation_rate = evaporation_rate

        # ========================================
        # setting the value of q
        self.q = q

        # ========================================
        # Initialize pheromone matrix
        self.pheromone = [[initial_pheromone for _ in range(num_cities)] for _ in range(num_cities)]

    # ==============================================================
    # Calculate the probability of moving to the next city
    def calculate_probabilities(self, current_city: int, unvisited: List[int]) -> List[float]:
        probabilities = []
        for city in unvisited:
            pheromone = self.pheromone[current_city][city] ** self.alpha
            distance = 1 / self.distance_func(current_city, city) ** self.beta
            probabilities.append(pheromone * distance)
        total = sum(probabilities)
        return [p / total for p in probabilities]

    # ==============================================================
    # Construct a solution for a single ant
    def construct_solution(self) -> List[int]:
        solution = [random.randint(0, self.num_cities - 1)]
        unvisited = list(set(range(self.num_cities)) - set(solution))

        while unvisited:
            current_city = solution[-1]
            probabilities = self.calculate_probabilities(current_city, unvisited)
            next_city = random.choices(unvisited, weights=probabilities)[0]
            solution.append(next_city)
            unvisited.remove(next_city)

        return solution

    # ==============================================================
    # Update pheromone levels
    def update_pheromone(self, solutions: List[List[int]], distances: List[float]):
        # Evaporation
        for i in range(self.num_cities):
            for j in range(self.num_cities):
                self.pheromone[i][j] *= (1 - self.evaporation_rate)

        # Deposit
        for solution, distance in zip(solutions, distances):
            for i in range(len(solution)):
                city1 = solution[i]
                city2 = solution[(i + 1) % len(solution)]
                self.pheromone[city1][city2] += self.q / distance
                self.pheromone[city2][city1] += self.q / distance

    # ==============================================================
    # Run the ACO algorithm for a specified number of iterations
    #
    # :param iterations: Number of iterations to run
    # :return: Best solution found
    def run(self, iterations: int) -> List[int]:
        best_solution = None
        best_distance = float('inf')

        for _ in range(iterations):
            solutions = [self.construct_solution() for _ in range(self.num_ants)]
            distances = [sum(self.distance_func(solution[i], solution[(i + 1) % len(solution)])
                             for i in range(len(solution))) for solution in solutions]

            self.update_pheromone(solutions, distances)

            iteration_best = min(zip(distances, solutions), key=lambda x: x[0])
            if iteration_best[0] < best_distance:
                best_distance, best_solution = iteration_best

        return best_solution