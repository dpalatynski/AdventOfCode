# Day 25
import networkx as nx
import math


def get_graph_edges(connections):
    edges = set()
    
    for line in connections:
        component, connections = line.split(':')
        connections = connections.split()
        
        for conn in connections:
            if (component, conn) not in edges:
                if (conn, component) not in edges:
                    edges.add((component, conn))
    
    return edges


def day25(my_input):
    diagram = my_input.split('\n')
    edges = get_graph_edges(diagram)

    graph = nx.Graph()
    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    cutsets = nx.minimum_edge_cut(graph)
    for node1, node2 in cutsets:
        graph.remove_edge(node1, node2)

    return math.prod([len(x) for x in nx.connected_components(graph)])


sample_input = '''jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr'''


# Test
assert(day25(sample_input) == 54)


# Results
my_input = open(r"2023/inputs/Day_25.txt").read()
print(day25(my_input))
