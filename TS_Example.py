# ==============================================================
# import the Class ACO
import Class_ACD as ACD
from typing import List

# ==============================================================
# Example usage: Solving Traveling Salesman Problem (TSP) using ACO
# Define the cities
cities = ['A', 'B', 'C', 'D']

# Define the weighted graph (distances) between cities
weights = {
    ('A', 'B'): 10, ('A', 'C'): 15, ('A', 'D'): 20,
    ('B', 'C'): 35, ('B', 'D'): 25,
    ('C', 'D'): 30
}

# ==============================================================
# Get the weight between two cities.
def get_weight(city1: int, city2: int) -> int:
    if city1 == city2:
        return 0
    city1_name = cities[city1]
    city2_name = cities[city2]
    if (city1_name, city2_name) in weights:
        return weights[(city1_name, city2_name)]
    if (city2_name, city1_name) in weights:
        return weights[(city2_name, city1_name)]
    raise ValueError(f"No weight defined for {city1_name} to {city2_name}")

# ==============================================================
# Initialize and run the Ant Colony Optimization algorithm
aco = ACD.AntColonyOptimization(
    num_ants=10,
    num_cities=len(cities),
    distance_func=get_weight,
    alpha=1.0,
    beta=2.0,
    evaporation_rate=0.5,
    q=100,
    initial_pheromone=1.0
)

best_solution = aco.run(iterations=100)

# Decode and print the best solution
best_route = [cities[i] for i in best_solution]
print("Best TSP Route:", ' -> '.join(best_route + [best_route[0]]))  # Add starting city at the end to complete the loop

# Calculate and print the total distance
total_distance = sum(get_weight(best_solution[i], best_solution[(i + 1) % len(best_solution)]) for i in range(len(best_solution)))
print("Total Distance:", total_distance)

# Print the distances between each pair of cities in the route
print("\nDistances between cities in the route:")
for i in range(len(best_route)):
    city1 = best_route[i]
    city2 = best_route[(i + 1) % len(best_route)]
    distance = get_weight(cities.index(city1), cities.index(city2))
    print(f"{city1} -> {city2}: {distance}")