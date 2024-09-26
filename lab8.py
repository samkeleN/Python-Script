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

edge_labels = nx.get_edge_attributes(G, 'weight')

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='red', edge_color='blue')
nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='red')

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
