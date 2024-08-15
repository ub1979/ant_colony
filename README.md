# Ant Colony Optimization Class

This repository contains a Python implementation of an Ant Colony Optimization (ACO) class and an example application solving the Traveling Salesman Problem (TSP).

## Contents

1. `ant_colony_optimization.py`: Contains the `AntColonyOptimization` class, a flexible implementation of the ACO algorithm.
2. `aco_tsp_example.py`: Demonstrates how to use the `AntColonyOptimization` class to solve a Traveling Salesman Problem.

## How to Use

### Requirements

* Python 3.6 or higher
* No additional libraries required

### Running the TSP Example

1. Clone this repository:

```
git clone https://github.com/yourusername/aco-tsp-solver.git
cd aco-tsp-solver
```

2. Run the TSP example:

```
python aco_tsp_example.py
```

This will execute the ACO algorithm to find an optimal solution for the TSP defined in the script.

### Using the AntColonyOptimization Class

To use the `AntColonyOptimization` class for your own problems:

1. Import the class:

```python
from ant_colony_optimization import AntColonyOptimization
```

2. Define your distance function. It should take two city indices as input and return the distance between them.

3. Initialize the ACO:

```python
aco = AntColonyOptimization(
    num_ants=10,
    num_cities=your_num_cities,
    distance_func=your_distance_function,
    alpha=1.0,
    beta=2.0,
    evaporation_rate=0.5,
    q=100,
    initial_pheromone=1.0
)
```

4. Run the algorithm:

```python
best_solution = aco.run(iterations=100)
```

5. Interpret the result based on your problem domain.

## Customization

* Modify the `alpha`, `beta`, `evaporation_rate`, and `q` parameters to fine-tune the algorithm's performance.
* Adjust the `num_ants` and number of `iterations` based on your problem's complexity and computational resources.
* For problems other than TSP, you may need to modify the `construct_solution` and `update_pheromone` methods in the `AntColonyOptimization` class.

## Contributing

Contributions to improve the algorithm or add new features are welcome. Please feel free to submit pull requests or open issues for any bugs or enhancements.

## License

This project is open-source and available under the MIT License.
