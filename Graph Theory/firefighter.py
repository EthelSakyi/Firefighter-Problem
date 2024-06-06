#Simulating the firefighter problem with k = 2 and 5 initially infected vertices
#At timestep 1 there are 2 fire fighters. 
import networkx as nx
import matplotlib.pyplot as plt

# Defining the size of the grid
rows, cols = 4, 5

# Creating the grid graph
G = nx.grid_2d_graph(rows, cols)

# Here are the initially infected vertices in coordinate form
initial_infected = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2)]

# The firefighter placements per time step
firefighter_placements = {
    1: [(0, 2), (1, 2)],
    2: [(3, 1), (3, 3)]
}

# Initializing the color map
color_map = {}
for node in G.nodes():
    if node in initial_infected:
        color_map[node] = 'red'
    else:
        color_map[node] = 'green'

# Helper function to update infection spread with firefighter intervention before the spread
def spread_fire(G, burning, protected):
    new_burning = set()
    for node in burning:
        for neighbor in G.neighbors(node):
            if neighbor not in burning and neighbor not in protected:
                new_burning.add(neighbor)
    return new_burning

def simulate_firefighter_intervention(G, initial_burning, firefighter_placements, steps):
    burning = set(initial_burning)
    protected = set()
    all_states = []

    for t in range(1, steps + 1):
        # Placing firefighters before infection spreads
        if t in firefighter_placements:
            for node in firefighter_placements[t]:
                protected.add(node)
                color_map[node] = 'blue'
        
        # Infection spreads after firefighters are placed
        new_burning = spread_fire(G, burning, protected)
        burning.update(new_burning)

        # Updating the color map for infected vertices
        for node in new_burning:
            color_map[node] = 'red'
        
        # Storing the state
        state_colors = [color_map[node] for node in G.nodes()]
        all_states.append(state_colors)

    return all_states

# To simulate the process...
all_states = simulate_firefighter_intervention(G, initial_infected, firefighter_placements, 2)

# Plotting each state...
pos = {(x, y): (y, -x) for x, y in G.nodes()}  # Positioning for better visualization

for t, state_colors in enumerate(all_states, start=1):
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, node_color=state_colors, with_labels=True, node_size=500)
    plt.title(f"Time Step {t}")
    plt.show()
    plt.pause(1)  # A pause to display the plot for 1 second (other timesteps will not show for some reason so added this to create a buffer)

# Final state plot
plt.figure(figsize=(10, 6))
nx.draw(G, pos, node_color=[color_map[node] for node in G.nodes()], with_labels=True, node_size=500)
plt.title("Final State")
plt.show()
