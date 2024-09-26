import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

G.add_edge(3, 1, weight=3)
G.add_edge(1, 4, weight=8)
G.add_edge(4, 5, weight=2)
G.add_edge(4, 0, weight=1)
G.add_edge(5, 0, weight=10)
G.add_edge(5, 2, weight=10)
G.add_edge(2, 0, weight=4)

shortest_path = nx.shortest_path(G, source=2, target=3, weight='weight')
shortest_distance = nx.shortest_path_length(G, source=2, target=3, weight='weight')

print("Shortest path from node 2 to node 3:", shortest_path)
print("Shortest distance:", shortest_distance)

pos = nx.spring_layout(G)

highlighted_edges = set(zip(shortest_path[:-1], shortest_path[1:]))  
edge_colors = ['green' if (u, v) in highlighted_edges or (v, u) in highlighted_edges else 'blue' for u, v in G.edges()]
edge_labels = nx.get_edge_attributes(G, 'weight')

nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='red', edge_color=edge_colors)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()