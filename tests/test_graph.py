import sys
sys.path.append("src")
from graph import Graph

print('Testing...')

edges = [(0, 1), (1, 2), (1, 3), (3, 4), (1, 4)]
vertices = ['a', 'b', 'c', 'd', 'e']
graph = Graph(edges, vertices)

print('    Node Indices:', [node.index for node in graph.nodes])
assert [node.index for node in graph.nodes] == [0, 1, 2, 3, 4], "the node's indices in graph are wrong and should be [0, 1, 2, 3, 4] but was {}".format([node.index for node in graph.nodes])

print('    Node Values:', [node.value for node in graph.nodes])
assert [node.value for node in graph.nodes] == ['a', 'b', 'c', 'd', 'e'], "the node's values in graph are wrong and should be [0, 1, 2, 3, 4] but was {}".format([node.value for node in graph.nodes])

print('    Number of Neighbors for each node:', [len(node.neighbors) for node in graph.nodes])
assert [len(node.neighbors) for node in graph.nodes] == [1, 4, 1, 2, 2], "the node's values in graph are wrong and should be [0, 1, 2, 3, 4] but was {}".format([node.value for node in graph.nodes])

print('    Depth First Search:', graph.depth_first_search(0))
assert graph.depth_first_search(0) == [0, 1, 2, 3, 4], "the search's values in graph are wrong and should be [0, 1, 2, 3, 4] but was {}".format(graph.depth_first_search(0))

print('All Tests PASS!!!')
