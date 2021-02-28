import networkx as nx
from sample import test_data_dict2
from networkx import pagerank 
from allgraph import allgraph_centrality_node as allgraph_c


def create_graph(dataset: dict):
    G = nx.Graph()
    for node in dataset.keys():
        G.add_node(node[0])
    for node in dataset.keys():
        for edge in dataset.get(node):
            G.add_edge(node[0], edge[0])
    return G

g = create_graph(test_data_dict2)
print('pagerank implementation in networkx:')
print('nodes:',g.nodes)
print('edges:',g.edges)
print('pagerank:',pagerank(g))
print('all graph centrality result for:')
c = allgraph_c(test_data_dict2)
print(c)

