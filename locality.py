from allgraph import allgraph_centrality_node

G = {
    ('v',): [('a',), ('b',), ('c',)],
    ('b',): [('v',)],
    ('a',): [('v',), ('d',)],
    ('c',): [('v',), ('e',)],
    ('e',): [('c',)],
    ('d',): [('a',)]
}

G_plus_e = {
    ('v',): [('a',), ('b',), ('c',)],
    ('b',): [('v',)],
    ('a',): [('v',), ('d',)],
    ('c',): [('v',), ('e',)],
    ('e',): [('c',)],
    ('d',): [('a',)],
    ('x',): [('y',), ('z',)],
    ('y',): [('x',)],
    ('z',): [('x',)],
}

print('computing centrality for G')
allgraph_centrality_node(G, ('v',))

print('----------------- Done -----------------')
print('computing centrality for G_plus_e')

allgraph_centrality_node(G_plus_e, ('v',))
print('----------------- Done -----------------')
