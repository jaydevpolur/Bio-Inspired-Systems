#Ant Colony Optimization (ACO) for TSP

import random
import numpy as np

# Example TSP Distance Matrix (symmetric)
distances = np.array([
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
])

def aco_tsp(distances, num_ants, num_iterations, alpha=1, beta=2, evaporation=0.5):
    num_cities = len(distances)
    pheromones = np.ones((num_cities, num_cities))
    best_path, best_cost = None, float('inf')

    for _ in range(num_iterations):
        all_paths = []
        for ant in range(num_ants):
            path = [random.randint(0, num_cities - 1)]
            while len(path) < num_cities:
                probabilities = []
                for j in range(num_cities):
                    if j not in path:
                        tau, eta = pheromones[path[-1]][j], 1 / distances[path[-1]][j]
                        probabilities.append((tau ** alpha) * (eta ** beta))
                    else:
                        probabilities.append(0)
                next_city = random.choices(range(num_cities), probabilities)[0]
                path.append(next_city)
            path.append(path[0])  # Return to the origin
            all_paths.append((path, sum(distances[path[i]][path[i+1]] for i in range(len(path)-1))))

        for path, cost in all_paths:
            if cost < best_cost:
                best_path, best_cost = path, cost

        pheromones *= (1 - evaporation)
        for path, cost in all_paths:
            for i in range(len(path) - 1):
                pheromones[path[i]][path[i+1]] += 1 / cost

    return best_path, best_cost

# Run ACO
best_path, best_cost = aco_tsp(distances, num_ants=10, num_iterations=100)
print("Student Name: Jaydev P")
print("USN: 1BM22CS118")
print(f"Best Path: {best_path}, Cost: {best_cost}")
