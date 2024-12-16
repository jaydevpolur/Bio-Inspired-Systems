#Genetic Algorithm for Optimization Problems
import random

name = "Jaydev P"
usn = "1BM22CS118"

def fitness_function(x):
    return -(x**2) + 10*x + 20

def generate_population(size, lower_bound, upper_bound):
    return [random.uniform(lower_bound, upper_bound) for _ in range(size)]

def select(population, fitness_scores, num_parents):
    parents = sorted(zip(population, fitness_scores), key=lambda x: x[1], reverse=True)
    return [p[0] for p in parents[:num_parents]]

def crossover(parents, offspring_size):
    offspring = []
    for _ in range(offspring_size):
        p1, p2 = random.sample(parents, 2)
        offspring.append((p1 + p2) / 2)
    return offspring

def mutate(offspring, mutation_rate, lower_bound, upper_bound):
    for i in range(len(offspring)):
        if random.random() < mutation_rate:
            offspring[i] += random.uniform(-1, 1)
            offspring[i] = max(min(offspring[i], upper_bound), lower_bound)
    return offspring

def genetic_algorithm(iterations, pop_size, lower_bound, upper_bound, num_parents, mutation_rate):
    population = generate_population(pop_size, lower_bound, upper_bound)
    for _ in range(iterations):
        fitness_scores = [fitness_function(x) for x in population]
        parents = select(population, fitness_scores, num_parents)
        offspring = crossover(parents, pop_size - num_parents)
        offspring = mutate(offspring, mutation_rate, lower_bound, upper_bound)
        population = parents + offspring
    best_solution = max(population, key=fitness_function)
    return best_solution, fitness_function(best_solution)

best_x, best_fitness = genetic_algorithm(iterations=50, pop_size=20, lower_bound=-10, upper_bound=10, num_parents=5, mutation_rate=0.2)

print("*******************************")
print(f"Student Name: {name}")
print(f"USN: {usn}")
print(f"Best Solution: x = {best_x:.2f}, Fitness = {best_fitness:.2f}")
print("*******************************")
