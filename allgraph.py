import math
import json
import random
import copy
import pandas as pd


'''
datastructure:
dictionary -> keys as nodes of graph and list of nodes for each node
each node represents in a tuple
'''


def neighborhood_graph(G: dict, v: tuple) -> dict:
    '''
    Create 1st neighborhood graph of node v from G
    :param G: graph
    :param v: node
    :return: neigborhood graph
    '''
    nodes = list(G.keys())
    if v in nodes:
        nodes.remove(v)  # do not consider node v in creating neighborhood for itself
    for u in nodes:
        if u not in G[v]:  # if u has no path to v (does not contains in its nodes connected list) then we have to remove it from graph
            for u_edge in G[u]: # remove edges for other nodes than v which their corresponding node is not present in neighborhood graph
                G.get(u_edge).remove(u)
            G.pop(u)

    return G



def count_all(G: dict, v: tuple) -> int:
    '''
    compute all graph centrality for node v in graph G
    :param G: graph
    :param v: node
    :return: int value of centrality (subgraph count)
    '''
    N = G.get(v, [])
    if N.__len__() == 0:
        return 1
    else:
        u = random.choice(N)
        W = 2 ** w(G, v, u) - 1
        R = remove(copy.deepcopy(G), u)
        S, _v = set_contraction(G, v, u)
        return count_all(R, v) + W * count_all(S, _v)


def count_trees(T: dict, v: tuple) -> int:
    '''
    compute all trees centrality for node v in tree T
    :param T: tree
    :param v: node
    :return: int value of centrality (subgraph count)
    '''
    N = T.get(v, [])
    if N.__len__() == 0:
        return 1
    else:
        u = random.choice(N)
        R = remove(copy.deepcopy(T), u)
        return count_trees(R, v) * (count_trees(R, u) + 1)


def add_node(G: dict, v: tuple, edgelist: list) -> dict:
    '''
    Add nodes v to graph G with list of edges
    :param G: graph
    :param v: node
    :param edgelist: list of nodes which v has edge to
    :return: updated graph G with added node
    '''
    G[v] = list(filter(lambda x: x in G.keys(), edgelist)) # add node to graph with edges which their node was present in graph (edges to non exist nodes will be filtered out)
    for edge in edgelist:
        if G.get(edge) is not None:
            G[edge].append(v) # add node v to edgelist of other nodes which has made edge to v
    return G


def remove(G: dict, v: tuple) -> dict:
    '''
    remove node v from graph G
    :param G: graph
    :param v: node
    :return: updated graph G
    '''
    if v not in G.keys():
        # when graph does not contain node v
        return G
    v_edges = G.get(v)  # get edges of node v
    G.pop(v)  # removing node v from graph
    for u in v_edges:
        # removing edges in graph which has been connected to node v
        try:
            G.get(u, []).remove(v)
        except Exception as e:
            print(e)

    return G


def set_contraction(G: dict, *U) -> tuple:
    '''
    combine nodes U in graph G
    :param G: graph
    :param U: list of nodes
    :return: updated graph and new node name (new supernode) with merged nodes
    '''
    merged_U_edges = [] # to keep edges to other nodes which edges in U had edge to
    new_node_name = () # to create a tuple containing merged node names (e.g. ('a','b'))
    #print(G)
    for u in U:
        u_edges = G.get(u, [])
        merged_U_edges.extend(u_edges)
        G = remove(G, u)
        new_node_name = new_node_name + u
    merged_U_edges = list(filter(lambda x: x not in U, merged_U_edges)) # filter nodes in edgelist of new node to remove edges between U edges inside its supernode
    #print(new_node_name)
    #print(merged_U_edges)
    G = add_node(G, new_node_name, merged_U_edges) # add new node graph with its corresponding edgelist
    #print(G)
    #print('*************************')
    return G, new_node_name


def w(G: dict, v, u) -> int:
    '''
    count edges between node v and u in graph G
    :param G: graph
    :param v: node
    :param u: node
    :return: int value of counted edges
    '''
    return G.get(v, []).count(u)


def test_set_contraction():
    graph = {
        ('v',): [('u',), ('u',), ('u',), ('y',)],
        ('u',): [('v',), ('v',), ('v',)],
        ('y',): [('v',)]
    }
    e = [('v',), ('u',)]
    print(json.dumps(set_contraction(graph, *e)))


def create_graph_from_dataset(file_path):
    '''
    create a graph with defined structure from key, value pair csv or txt file
    :param file_path: path of dataset
    :return: graph G
    '''
    data = pd.read_csv(file_path, delimiter=' ', header=None)
    data = data.iloc[:].values
    data_dict = {}
    for i in data:
        key = (str(i[0]),)
        value = (str(i[1]),)
        if key not in data_dict.keys():
            data_dict[key] = [value]
        else:
            data_dict[key].append(value)

    return data_dict


def allgraph_centrality_dataset(file_path):
    '''
    compute allgraph centrality on random node from a dataset file
    :param file_path: path of dataset
    :return:
    '''
    G = create_graph_from_dataset(file_path)
    vertex = random.choice(list(G.keys()))
    allgraph_centrality_node(G, vertex)


def allgraph_centrality_node(data_dict, vertex):
    '''
    compute allgraph centrality on given node for given graph
    :param file_path: path of dataset
    :return:
    '''
    a = count_all(data_dict, vertex)
    print(f'centrality for node v in graph is {a}')
    print(f'log centrality for node v in graph is {math.log(a)}')
    return a


def compute_centrality(G, centrality=count_all) -> dict:
    '''
    compute allgraph centrality for all nodes in graph G
    :param G: graph
    :return: key value pair dictionary containing nodes with centrality value
    '''
    centralities = {}
    for v in G.keys():
        centralities[v] = centrality(copy.deepcopy(G), v)
    sum_c = sum(centralities.values())
    for c in centralities:
        centralities[c] = centralities[c]/sum_c
    return centralities


def allgraph_centrality(G: dict) -> dict:
    return compute_centrality(G, count_all)

def alltree_centrality(T: dict) -> dict:
    return compute_centrality(T, count_trees)
