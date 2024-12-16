#Grey Wolf Optimizer (GWO)

import numpy as np

def objective_function(x):
    return np.sum(x**2)

def gwo(num_wolves, dimensions, max_iter):
    alpha_pos = np.zeros(dimensions)
    beta_pos = np.zeros(dimensions)
    delta_pos = np.zeros(dimensions)
    alpha_score, beta_score, delta_score = float("inf"), float("inf"), float("inf")

    wolves = np.random.uniform(-10, 10, (num_wolves, dimensions))

    for _ in range(max_iter):
        for i in range(num_wolves):
            fitness = objective_function(wolves[i])
            if fitness < alpha_score:
                delta_score, delta_pos = beta_score, beta_pos.copy()
                beta_score, beta_pos = alpha_score, alpha_pos.copy()
                alpha_score, alpha_pos = fitness, wolves[i].copy()
            elif fitness < beta_score:
                delta_score, delta_pos = beta_score, beta_pos.copy()
                beta_score, beta_pos = fitness, wolves[i].copy()
            elif fitness < delta_score:
                delta_score, delta_pos = fitness, wolves[i].copy()

        a = 2 - _ * (2 / max_iter)
        for i in range(num_wolves):
            for j in range(dimensions):
                r1, r2 = np.random.random(), np.random.random()
                A1 = 2 * a * r1 - a
                C1 = 2 * r2
                D_alpha = abs(C1 * alpha_pos[j] - wolves[i, j])
                X1 = alpha_pos[j] - A1 * D_alpha

                r1, r2 = np.random.random(), np.random.random()
                A2 = 2 * a * r1 - a
                C2 = 2 * r2
                D_beta = abs(C2 * beta_pos[j] - wolves[i, j])
                X2 = beta_pos[j] - A2 * D_beta

                r1, r2 = np.random.random(), np.random.random()
                A3 = 2 * a * r1 - a
                C3 = 2 * r2
                D_delta = abs(C3 * delta_pos[j] - wolves[i, j])
                X3 = delta_pos[j] - A3 * D_delta

                wolves[i, j] = (X1 + X2 + X3) / 3

    print("Name: Jaydev P\nUSN: 1BM22CS118")
    print(f"Best Solution: {alpha_pos}, Best Fitness: {alpha_score}")

gwo(num_wolves=5, dimensions=5, max_iter=100)
