
import networkx as nx
import matplotlib.pyplot as plt
import random

# Create a 6x6 grid graph
G = nx.grid_2d_graph(6, 6)
pos = dict((n, n) for n in G.nodes())

# Randomly select an initial infected vertex
initial_infected = random.choice(list(G.nodes()))

# Function to draw the graph
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

        # Spread the fire to adjacent nodes
        for node in infected:
            for neighbor in G.neighbors(node):
                if neighbor not in infected and neighbor not in protected:
                    new_infected.add(neighbor)

        infected.update(new_infected)

        # Firefighters protect uninfected nodes
        for _ in range(num_firefighters):
            uninfected_nodes = set(G.nodes()) - infected - protected
            if uninfected_nodes:
                firefighter_position = random.choice(list(uninfected_nodes))
                protected.add(firefighter_position)

        if not new_infected:
            break
    
    return timesteps, len(protected)

# Initial infected vertex
initial_infected = random.choice(list(G.nodes()))

# Run simulation with 3 firefighters
timesteps_3, protected_3 = simulate_firefighters(3, initial_infected)
# Run simulation with 4 firefighters
timesteps_4, protected_4 = simulate_firefighters(4, initial_infected)

print("3 Firefighters: Timesteps =", timesteps_3, ", Protected Vertices =", protected_3)
print("4 Firefighters: Timesteps =", timesteps_4, ", Protected Vertices =", protected_4)

