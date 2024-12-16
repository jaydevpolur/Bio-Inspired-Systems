#Parallel Cellular Algorithm

import numpy as np

def objective_function(x):
    return np.sum(x**2)

def parallel_cellular_algorithm(grid_size, iterations):
    grid = np.random.uniform(-10, 10, (grid_size, grid_size))
    best_solution = float("inf")

    for _ in range(iterations):
        new_grid = grid.copy()
        for i in range(grid_size):
            for j in range(grid_size):
                neighbors = [
                    grid[(i-1) % grid_size, j],
                    grid[(i+1) % grid_size, j],
                    grid[i, (j-1) % grid_size],
                    grid[i, (j+1) % grid_size]
                ]
                new_grid[i, j] = np.mean(neighbors) + np.random.uniform(-0.1, 0.1)
        grid = new_grid
        current_best = np.min(grid)
        best_solution = min(best_solution, current_best)

    print("Name: Jaydev P\nUSN: 1BM22CS118")
    print(f"Best Solution: {best_solution}")

parallel_cellular_algorithm(grid_size=5, iterations=50)
