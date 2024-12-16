#Parallel Cellular Algorithms Implementation

import numpy as np

def define_problem():
    """Define a sample mathematical problem: Sphere function"""
    def sphere_function(position):
        return sum(x**2 for x in position)
    return sphere_function

def initialize_parameters():
    """Initialize grid parameters"""
    params = {
        'grid_size': (10, 10),  # Grid of 10x10 cells
        'num_iterations': 100,
        'neighbor_radius': 1,
        'lower_bound': -10,
        'upper_bound': 10,
        'dimensions': 2,  # Each solution has 2 dimensions
    }
    return params

def initialize_population(grid_size, lower_bound, upper_bound, dimensions):
    """Initialize the grid with random positions"""
    return np.random.uniform(lower_bound, upper_bound, size=grid_size + (dimensions,))

def evaluate_fitness(grid, fitness_function):
    """Evaluate fitness for each cell"""
    return np.apply_along_axis(fitness_function, -1, grid)

def get_neighbors(grid, x, y, radius):
    """Retrieve neighbors within a given radius"""
    neighbors = []
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            if i == 0 and j == 0:
                continue
            nx, ny = (x + i) % grid.shape[0], (y + j) % grid.shape[1]
            neighbors.append(grid[nx, ny])
    return neighbors

def update_states(grid, fitness_function, neighbor_radius):
    """Update each cell based on neighbors' states"""
    new_grid = grid.copy()
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            neighbors = get_neighbors(grid, x, y, neighbor_radius)
            best_neighbor = min(neighbors, key=fitness_function)
            if fitness_function(best_neighbor) < fitness_function(grid[x, y]):
                new_grid[x, y] = best_neighbor
    return new_grid

def parallel_cellular_algorithm():
    """Main function to execute the Parallel Cellular Algorithm"""
    fitness_function = define_problem()
    params = initialize_parameters()

    grid = initialize_population(
        params['grid_size'],
        params['lower_bound'],
        params['upper_bound'],
        params['dimensions']
    )

    for iteration in range(params['num_iterations']):
        grid = update_states(grid, fitness_function, params['neighbor_radius'])
        fitness_values = evaluate_fitness(grid, fitness_function)
        best_solution = np.unravel_index(np.argmin(fitness_values), fitness_values.shape)

    print("Name: Jaydev P\nUSN: 1BM22CS118")
    print("Final Best Solution:", grid[best_solution])

parallel_cellular_algorithm()

