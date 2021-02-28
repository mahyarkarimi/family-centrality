import itertools
import pprint
import random
from copy import deepcopy

import math

from allgraph import neighborhood_graph, set_contraction, create_graph_from_dataset
from sample import test_data_dict2


def all_combinations(any_list):
    '''
    get all combinations of items in a set
    :param any_list:
    :return:
    '''
    return itertools.chain.from_iterable(
        itertools.combinations(any_list, i + 1)
        for i in range(len(any_list)))


def add_subgraphs(subgraphs1: list, subgraphs2: list):
    '''
    add subgraphs2 to subgraphs1 with removing duplicates
    :param subgraphs1: list of subgraphs
    :param subgraphs2: list of subgraphs
    :return:
    '''
    s1 = list(map(lambda s: set(s), set(subgraphs1)))
    s2 = list(map(lambda s: set(s), set(subgraphs2)))
    
    intersection = []
    for i in s2:
        intersection.extend(list(filter(lambda x: x==i, s1)))
    
    for i in intersection:
        subgraphs1 = list(filter(lambda subgraph: set(subgraph) != i, subgraphs1))
    subgraphs1.extend(subgraphs2)
    return subgraphs1


def count_graph_gen(G:dict, v:tuple) -> int:
    '''
    compute centrality with generation method
    :param G: graph
    :param v: node
    :return:
    '''
    subgraphs = list()
    graphs = [(G, v)]
    
    while len(graphs) > 0:
        print(graphs[0])
        g = graphs[0][0]
        _v = graphs[0][1]
        N = neighborhood_graph(deepcopy(g), _v)
        print('N:', N)
        v_subgraphs = [_v + tuple(itertools.chain(*l)) for l in all_combinations(g[_v])]
        subgraphs = add_subgraphs(subgraphs, v_subgraphs)
        print('centrality:', len(subgraphs))
        v_edges = N.get(_v)
        non_ending_nodes = []
        for u in set(v_edges):
            u_edges = set(itertools.chain(*g.get(u)))
            if u_edges.difference(set(_v)).__len__() > 0:
                non_ending_nodes.append(u)
        print('non_ending_nodes:', non_ending_nodes)
        for i in range(1, len(non_ending_nodes) + 1):
            for possibility in list(itertools.combinations(non_ending_nodes, i)):
                print(possibility)
                _g, __v = set_contraction(deepcopy(g), _v, *possibility)
                graphs.append((_g, __v))
                del _g, __v
        graphs.pop(0)
        del non_ending_nodes
    print('**********************')
    pprint.pprint(subgraphs)
    print('**********************')

    return len(subgraphs) + 1


def run_alg3_test_graph():
    a = count_graph_gen(test_data_dict2, ('v',))
    print(f'centrality for node v in graph is {a}')
    print(f'log centrality for node v in graph is {math.log(a)}')


def run_facebook_ego():
    G = create_graph_from_dataset('./facebook/0.edges')
    vertex = random.choice(list(G.keys()))
    a = count_graph_gen(G, vertex)
    print(f'centrality for node {vertex} in graph is {a}')
    print(f'log centrality for node {vertex} in graph is {math.log(a)}')


def compute_centrality(G) -> dict:
    '''
    compute allgraph centrality for all nodes in graph G with usage of generation method for subgraph counting
    :param G: graph
    :return: key value pair dictionary containing nodes with centrality value
    '''
    centralities = {}
    for v in G.keys():
        centralities[v] = count_graph_gen(deepcopy(G), v)
    sum_c = sum(centralities.values())
    for c in centralities:
        centralities[c] = centralities[c]/sum_c
    return centralities
