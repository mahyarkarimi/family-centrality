import pandas as pd
import json, random

data = pd.read_csv('Email-Enron.csv', delimiter='	')
# print([data.iloc[] for i in data.iloc[:,1] if i==1])
# print(set(data.iloc[:,1]))
data = data.iloc[:].values
vertex = random.choice(data[:, 0])
vertex = 1
data_dict = {}

'''
make graph data model as a dictionary with nodes as keys and connected nodes list as values; e.g.
{
    1: [1, 2, 3],
    2: [1],
    3: [2]
}
'''
for i in data:
    key = int(i[0])
    value = int(i[1])
    if key not in data_dict.keys():
        data_dict[key] = [value]
    else:
        data_dict[key].append(value)


def neighborhood(G: dict, v) -> dict:
    nodes = list(G.keys())
    nodes.remove(v)  # do not consider node v in creating neighborhood for itself
    for u in nodes:
        if u not in G[v]:  # if u has no path to v (does not contains in its nodes connected list) then we have to remove it from graph
            G.pop(u)
    return G


def count_all(G: dict, v) -> int:
    if neighborhood(G, v).keys().__len__() == 0:
        return 1
    else:
        pass



def remove(G: dict, v) -> dict:
    # remove node v from graph G
    if not G.get(v):
        # when graph does not contain node v
        print('graph does not contain node ', v)
        return G
    v_edges = G.get(v) # get edges of node v
    G.pop(v) # removing node v from graph
    for u in v_edges:
        # removing edges in graph which has been connected to node v
        G.get(u, []).remove(v)

    return G


def set_contraction(G: dict, U: list):
    merged_U_edges = []
    for u in U:
        u_edges = G.get(u)
        merged_U_edges.extend([i for i in u_edges if not U.__contains__(i)])
        G = remove(G, u)

    new_node_name = random.choice(U)
    G[new_node_name] = merged_U_edges
    for i in merged_U_edges:
        G.get(i).append(new_node_name)
    return G


def test_set_contraction():
    graph = {
        'v': ['u', 'u', 'u', 'y'],
        'u': ['v', 'v', 'v'],
        'y': ['v']
    }
    e = ['v', 'u']
    print(json.dumps(set_contraction(graph, e)))


test_set_contraction()
# print('vertex: ', vertex)
# print(json.dumps(remove(data_dict, vertex), indent=4))
# print(json.dumps(neighborhood(data_dict, vertex), indent=4))