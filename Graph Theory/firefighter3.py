#With only 3 firefighters, it is impossible to fully contain the fire because there will always
#be at least one unprotected direction. Proof by contradiction that 4 firefighters are enough for 
# d >= 2
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation
import random

# Create a strong grid graph (4x5)
def create_strong_grid_graph(rows, cols):
    G = nx.grid_2d_graph(rows, cols)
    for i in range(rows):
        for j in range(cols):
            if i < rows - 1 and j < cols - 1:
                G.add_edge((i, j), (i + 1, j + 1))
            if i < rows - 1 and j > 0:
                G.add_edge((i, j), (i + 1, j - 1))
    return G

G = create_strong_grid_graph(4, 5)

# Initial fire position
initial_fire = (2, 2)

# Randomly pick three different firefighter positions
available_positions = list(G.nodes)
available_positions.remove(initial_fire)
firefighters = random.sample(available_positions, 3)

# Initialize fire status
fire_status = {node: False for node in G.nodes()}
fire_status[initial_fire] = True

# Initialize firefighter positions
firefighter_positions = {node: False for node in G.nodes()}
for firefighter in firefighters:
    firefighter_positions[firefighter] = True

# Colors for the nodes
def get_node_colors():
    colors = []
    for node in G.nodes():
        if fire_status[node]:
            colors.append('red')
        elif firefighter_positions[node]:
            colors.append('blue')
        else:
            colors.append('green')
    return colors

def update(num):
    global G, fire_status

    # Spread the fire
    new_fire = []
    for node in G.nodes():
        if fire_status[node]:
            for neighbor in G.neighbors(node):
                if not fire_status[neighbor] and not firefighter_positions[neighbor]:
                    new_fire.append(neighbor)

    for fire in new_fire:
        fire_status[fire] = True

    # Update colors
    node_colors = get_node_colors()
    ax.clear()
    nx.draw(G, pos, node_color=node_colors, with_labels=True, font_weight='bold')
    ax.set_title(f"Timestep {num}")

fig, ax = plt.subplots()
pos = {(i, j): (j, -i) for i, j in G.nodes()}
node_colors = get_node_colors()
nx.draw(G, pos, node_color=node_colors, with_labels=True, font_weight='bold')
ani = FuncAnimation(fig, update, frames=10, interval=2000, repeat=False)
plt.show()


#The infection starts at (2,2) and the 3 firefighters are positioned at (1,2) (2,1), and (3,2)
#The infection spreads to (2,3) and (3,1) which are unprotected 
#The fire continues to spread in the subsequent turns, demonstrating that three firefighters are insufficient to contain the fire.
#Check 3 on a finite graph 
#how can we save the maximum 
#area vs perimeter