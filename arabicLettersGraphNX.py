#pip install arabic-reshaper python-bidi

import networkx as nx
import matplotlib.pyplot as plt
from arabic_reshaper import reshape
from bidi.algorithm import get_display

# Créer un graphe vide
G = nx.Graph()

# Ajouter des nœuds (individus dans un réseau) en arabe
arabic_name_1 = get_display(reshape('عبدالناصر'))
arabic_name_2 = get_display(reshape('محمد'))
arabic_name_3 = get_display(reshape('هشام'))
arabic_name_4 = get_display(reshape('إ'))
arabic_name_5 = get_display(reshape('ب'))
arabic_name_P = get_display(reshape('بدء'))
arabic_name_S = get_display(reshape('انتهاء'))

G.add_node(arabic_name_1)
G.add_node(arabic_name_2)
G.add_node(arabic_name_4)
G.add_node(arabic_name_5)
G.add_node(arabic_name_P)
G.add_node(arabic_name_S)

# Ajouter des arêtes (connexions entre individus)
G.add_edge(arabic_name_1, arabic_name_P)
G.add_edge(arabic_name_4, arabic_name_P)
G.add_edge(arabic_name_P, arabic_name_S)
G.add_edge(arabic_name_S, arabic_name_2)
G.add_edge(arabic_name_S, arabic_name_3)
G.add_edge(arabic_name_S, arabic_name_5)

# Dessiner le graphe
nx.draw(G, with_labels=True, node_color='skyblue', font_family='sans-serif')
plt.show()
