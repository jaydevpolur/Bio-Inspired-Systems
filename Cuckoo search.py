#Cuckoo search(CS)

import numpy as np
import math

def objective_function(x):
    return np.sum(x**2)

def levy_flight(Lambda):
    sigma = (math.gamma(1 + Lambda) * np.sin(np.pi * Lambda / 2) /
             (math.gamma((1 + Lambda) / 2) * Lambda * 2**((Lambda - 1) / 2)))**(1 / Lambda)
    u = np.random.normal(0, sigma, size=(2,))
    v = np.random.normal(0, 1, size=(2,))
    step = u / abs(v)**(1 / Lambda)
    return step

def cuckoo_search(nests, iterations, pa):
    n = len(nests)
    alpha = 0.01
    best_nest = nests[np.argmin([objective_function(nest) for nest in nests])]
    
    for _ in range(iterations):
        new_nests = nests.copy()
        for i in range(n):
            step_size = levy_flight(1.5)
            new_nests[i] += step_size * (nests[i] - best_nest) * alpha
            new_nests[i] = np.clip(new_nests[i], -10, 10)
            if objective_function(new_nests[i]) < objective_function(nests[i]):
                nests[i] = new_nests[i]
        
        for i in range(n):
            if np.random.random() < pa:
                nests[i] = np.random.uniform(-10, 10, size=(2,))
                
        best_nest = nests[np.argmin([objective_function(nest) for nest in nests])]
    
    print("Name: Jaydev P\nUSN: 1BM22CS118")
    print(f"Best Solution: {best_nest}, Best Fitness: {objective_function(best_nest)}")

nests = np.random.uniform(-10, 10, (10, 2))
cuckoo_search(nests=nests, iterations=100, pa=0.25)
