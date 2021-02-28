from allgraph import allgraph_centrality_node, add_node
from copy import deepcopy
g = {
    ('v',): [],
}
G = {
    ('v',): [('a',), ('b',), ('c',)],
    ('b',): [('v',)],
    ('a',): [('v',), ('d',)],
    ('c',): [('v',), ('e',)],
    ('e',): [('c',)],
    ('d',): [('a',)]
}

# creating G from g by adding vertices and edges to it
import pprint
centralities = []
for node in list(G.keys()):
    if node == ('v',): continue
    g = add_node(g, node, G[node])
    print(f'computing centrality for node v in g={g}')
    C_v = allgraph_centrality_node(deepcopy(g), ('v',))
    centralities.append(f'In g={g} ==>> C(v)={C_v}')
print(centralities)
