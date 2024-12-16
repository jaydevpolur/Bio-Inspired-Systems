#Particle Swarm Optimization (PSO)

import random

def fitness_function(x):
    return x**2 - 4*x + 4

class Particle:
    def __init__(self):
        self.position = random.uniform(-10, 10)
        self.velocity = random.uniform(-1, 1)
        self.best_position = self.position
        self.best_fitness = fitness_function(self.position)

def pso_algorithm(num_particles=10, num_iterations=50):
    particles = [Particle() for _ in range(num_particles)]
    global_best_position = min(particles, key=lambda p: p.best_fitness).best_position

    for iteration in range(num_iterations):
        for particle in particles:
            fitness = fitness_function(particle.position)
            if fitness < particle.best_fitness:
                particle.best_fitness = fitness
                particle.best_position = particle.position

            if fitness < fitness_function(global_best_position):
                global_best_position = particle.position

            inertia = 0.5
            cognitive_component = 1.5 * random.random() * (particle.best_position - particle.position)
            social_component = 1.5 * random.random() * (global_best_position - particle.position)
            particle.velocity = inertia * particle.velocity + cognitive_component + social_component
            particle.position += particle.velocity

    print("Student Name: Jaydev P")
    print("USN: 1BM22CS118")
    print("Optimal Solution Found (Global Best Position):", global_best_position)
    print("Fitness at Global Best Position:", fitness_function(global_best_position))

pso_algorithm()
