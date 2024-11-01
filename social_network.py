import networkx as nx
from matplotlib import pyplot as plt
from networkx.algorithms import community

#1: graph khawi

G = nx.Graph()

# add nodes
users = ["Nacer", "Mohamed", "Hicham", "Abdellatif", "Fouad", "Ossama"]
G.add_nodes_from(users)

G.add_edge("Nacer", "Mohamed", weight =5 )
G.add_edge("Nacer", "Hicham", weight = 3)
G.add_edge("Nacer", "Abdellatif", weight =2 )
G.add_edge("Abdellatif", "Fouad", weight = 4)
#G.add_edge("Nacer", "Ossama", weight = 2)
G.add_edge("Hicham", "Ossama", weight = 7)
G.add_edge("Hicham", "Fouad", weight = 7)
G.add_edge("Fouad", "Ossama", weight = 2)
G.add_edge("Mohamed", "Abdellatif", weight = 1)

# werri lgraph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels = True, node_color="skyblue", node_size=1500, font_size=8)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Graph dial chabaka")


# daraja taetir
degree_centrality = nx.degree_centrality(G)
print("Degree Centrality dial kol wa7ed: ")
for user, centrality in degree_centrality.items():
    print(f"{user}: {centrality:.2f}")

# asgher tri9
shortest_path = nx.shortest_path(G, source = "Nacer", target= "Ossama", weight = "weight")
print("Shortes Path, from Nacer to Ossama: ")
print("\n".join(shortest_path))

#
print("3ala9at wazina")
for u, v, data in G.edges(data=True):
    print(f"{u} - {v}, Weight: {data['weight']}")

# 
communities = community.greedy_modularity_communities(G)
print("Majtama3at: ")
for i, moj in enumerate(communities):
    print(f"Mojtama3 {i + 1}: {', '.join(moj)}")


# werri flekher
plt.show()
plt.pause(2)
plt.close()

# Detect communities and visualize each community separately
communities = community.greedy_modularity_communities(G)
# Visualize each community separately in its own figure
for i, comm in enumerate(communities):
    plt.figure(figsize=(6, 4))
    comm_subgraph = G.subgraph(comm)
    pos = nx.spring_layout(comm_subgraph)
    nx.draw(comm_subgraph, pos, with_labels=True, node_color="lightgreen", node_size=1500, font_size=10)
    labels = nx.get_edge_attributes(comm_subgraph, "weight")
    nx.draw_networkx_edge_labels(comm_subgraph, pos, edge_labels=labels)
    plt.title(f"Graph dial Mojtama3 {i + 1}")

# Show all plots at once
plt.show()