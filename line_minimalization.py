from allgraph import allgraph_centrality_node
from copy import deepcopy
G = {
    ('a',): [('b',)],
    ('b',): [('a',), ('c',)],
    ('c',): [('b',), ('d',)],
    ('d',): [('c',)]
}

print('computing centrality for G')
C_a = allgraph_centrality_node(deepcopy(G), ('a',))
C_b = allgraph_centrality_node(deepcopy(G), ('b',))
C_c = allgraph_centrality_node(deepcopy(G), ('c',))
C_d = allgraph_centrality_node(deepcopy(G), ('d',))
print(f'C(a)={C_a} || C(b)={C_b} || C(c)={C_c} || C(d)={C_d}')
print('----------------- Done -----------------')
