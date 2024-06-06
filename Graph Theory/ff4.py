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

# Firefighters' positions
firefighters = []

# Lists to track infected and protected nodes
infected = {initial_infected}
protected = set()

# Number of timesteps
timesteps = 0
max_timesteps = 36  # Maximum timesteps to avoid infinite loop in worst case

# Simulation loop
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
    for _ in range(3):
        uninfected_nodes = set(G.nodes()) - infected - protected
        if uninfected_nodes:
            firefighter_position = random.choice(list(uninfected_nodes))
            protected.add(firefighter_position)
    
    # Draw the graph at current timestep
    draw_graph(G, pos, infected, protected, timesteps)
    
    if not new_infected:
        break

timesteps
