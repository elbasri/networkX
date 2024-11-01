#pip install networkx
import networkx as nx
import matplotlib.pyplot as plt

# Créer un graphe vide
G = nx.Graph()
# Ajouter des nœuds (individus dans un réseau)
G.add_node('Nacer')
G.add_node('Mohamed')
G.add_node('Hicham')
# Ajouter des arêtes (connexions entre individus)
G.add_edge('Nacer', 'Mohamed')
G.add_edge('Nacer', 'Hicham')
G.add_edge('Mohamed', 'Hicham')
# Dessiner le graphe
nx.draw(G, with_labels=True)
plt.show()