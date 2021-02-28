from allgraph import allgraph_centrality_node
from copy import deepcopy
G = {
    ('v',): [('a',), ('b',), ('c',)],
    ('b',): [('v',)],
    ('a',): [('v',), ('d',)],
    ('c',): [('v',), ('e',)],
    ('e',): [('c',)],
    ('d',): [('a',)]
}

G_plus_e = {
    ('v',): [('a',), ('b',), ('c',), ('e',)],
    ('b',): [('v',)],
    ('a',): [('v',), ('d',)],
    ('c',): [('v',), ('e',)],
    ('e',): [('c',), ('v',)],
    ('d',): [('a',)]
}
print('computing centrality for G')
C_v = allgraph_centrality_node(deepcopy(G), ('v',))
C_a = allgraph_centrality_node(deepcopy(G), ('a',))
print(f'C(v)={C_v} || C(a)={C_a}')
print('----------------- Done -----------------')
print('computing centrality for G_plus_e')
C_v = allgraph_centrality_node(deepcopy(G_plus_e), ('v',))
C_a = allgraph_centrality_node(deepcopy(G_plus_e), ('a',))
print(f'C(v)={C_v} || C(a)={C_a}')
print('----------------- Done -----------------')