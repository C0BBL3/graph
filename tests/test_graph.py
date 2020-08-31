import sys
sys.path.append("src")
from graph import Graph

print('\nTesting...')

edges = [(0, 1), (1, 2), (1, 3), (3, 4), (1, 4)]
vertices = ['a', 'b', 'c', 'd', 'e']
graph = Graph(edges, vertices)

print('\n    Node Indices:', [node.index for node in graph.nodes])
assert [node.index for node in graph.nodes] == [0, 1, 2, 3, 4], "the node's indices in graph are wrong and should be [0, 1, 2, 3, 4] but was {}".format([node.index for node in graph.nodes])

print('\n    Node Values:', [node.value for node in graph.nodes])
assert [node.value for node in graph.nodes] == ['a', 'b', 'c', 'd', 'e'], "the node's values in graph are wrong and should be [0, 1, 2, 3, 4] but was {}".format([node.value for node in graph.nodes])

print('\n    Number of Neighbors for each node:', [len(node.neighbors) for node in graph.nodes])
assert [len(node.neighbors) for node in graph.nodes] == [1, 4, 1, 2, 2], "the node's values in graph are wrong and should be [0, 1, 2, 3, 4] but was {}".format([node.value for node in graph.nodes])

print('\n    Depth First Search:', graph.depth_first_search(0))
assert graph.depth_first_search(0) == [0, 1, 2, 3, 4], "the search's values in graph are wrong and should be [0, 1, 2, 3, 4] but was {}".format(graph.depth_first_search(0))

print('\n    Breath First Search:', graph.breadth_first_search(1))
assert graph.breadth_first_search(1) == [1, 0, 2, 3, 4], "the search's values in graph are wrong and should be [0, 1, 2, 3, 4] but was {}".format(graph.breadth_first_search(1))

print('\n    Find Distance tests...')
edges = [(0, 1), (1, 2), (1, 3), (3, 4), (1, 4), (4, 5)]
vertices = ['a', 'b', 'c', 'd', 'e', 'f']
graph = Graph(edges, vertices)
print('\n        Find Distance (0, 4):', graph.find_distance(0, 4))  # 2
assert graph.find_distance(0, 4) == 2, "find_distance() should be 2, but was {}".format(graph.find_distance(0, 4))
print('        Find Distance (5, 2):', graph.find_distance(5, 2))  # 3
assert graph.find_distance(5, 2) == 3, "find_distance() should be 3, but was {}".format(graph.find_distance(5, 2))
print('        Find Distance (0, 5):', graph.find_distance(0, 5))  # 3
assert graph.find_distance(0, 5) == 3, "find_distance() should be 3, but was {}".format(graph.find_distance(0, 5))
print('        Find Distance (4, 1):', graph.find_distance(4, 1))  # 1
assert graph.find_distance(4, 1) == 1, "find_distance() should be 1, but was {}".format(graph.find_distance(4, 1))
print('        Find Distance (3, 3):', graph.find_distance(3, 3))  # 0
assert graph.find_distance(3, 3) == 0, "find_distance() should be 0, but was {}".format(graph.find_distance(3, 3))
print('\n    Find Distance Tests PASS!!!')


print('\nAll Tests PASS!!!')
