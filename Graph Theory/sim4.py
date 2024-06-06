#runs multiple simulations (100 by default) and compares the average 
#number of protected vertices for 3 firefighters and 4 firefighters. It also counts 
#how many times 4 firefighters protected more vertices compared to 3 firefighters
import networkx as nx
import matplotlib.pyplot as plt
import random

# Creating a 6x6 grid graph
G = nx.grid_2d_graph(6, 6)
pos = dict((n, n) for n in G.nodes())

# This function should draw the graph
def draw_graph(G, pos, infected, protected, timestep):
    plt.figure(figsize=(8, 8))
    node_colors = []
    for node in G.nodes():
        if node in infected:
            node_colors.append('red')
        elif node in protected:
            node_colors.append('blue')
        else:
            node_colors.append('green')
    
    nx.draw(G, pos, node_color=node_colors, with_labels=True, node_size=600, font_size=10)
    plt.title(f"Timestep {timestep}")
    plt.show()

def simulate_firefighters(num_firefighters, initial_infected):
    infected = {initial_infected}
    protected = set()
    timesteps = 0
    max_timesteps = 36

    while infected and timesteps < max_timesteps:
        timesteps += 1
        new_infected = set()

        # Spreading the infection to adjacent vertices 
        for node in infected:
            for neighbor in G.neighbors(node):
                if neighbor not in infected and neighbor not in protected:
                    new_infected.add(neighbor)

        infected.update(new_infected)

        # Let the firefighters protected the uninfected vertices they can 
        for _ in range(num_firefighters):
            uninfected_nodes = set(G.nodes()) - infected - protected
            if uninfected_nodes:
                firefighter_position = random.choice(list(uninfected_nodes))
                protected.add(firefighter_position)

        if not new_infected:
            break
    
    return timesteps, len(protected)

def run_multiple_simulations(num_simulations):
    results_3 = []
    results_4 = []
    for _ in range(num_simulations):
        initial_infected = random.choice(list(G.nodes()))
        _, protected_3 = simulate_firefighters(3, initial_infected)
        _, protected_4 = simulate_firefighters(4, initial_infected)
        results_3.append(protected_3)
        results_4.append(protected_4)
    return results_3, results_4

# Run the multiple simulations for data collection
num_simulations = 100
results_3, results_4 = run_multiple_simulations(num_simulations)

# Calculating average protected vertices
avg_protected_3 = sum(results_3) / num_simulations
avg_protected_4 = sum(results_4) / num_simulations

print(f"Average protected vertices with 3 firefighters: {avg_protected_3}")
print(f"Average protected vertices with 4 firefighters: {avg_protected_4}")

# Comparison of the results 
more_protected_4 = sum(p4 > p3 for p3, p4 in zip(results_3, results_4))
equal_protected = sum(p4 == p3 for p3, p4 in zip(results_3, results_4))

print(f"4 firefighters protected more vertices in {more_protected_4} out of {num_simulations} simulations.")
print(f"Both protected the same number of vertices in {equal_protected} out of {num_simulations} simulations.")
