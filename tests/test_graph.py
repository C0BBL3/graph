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

print('\n    Calculate Distance tests...')
edges = [(0, 1), (1, 2), (1, 3), (3, 4), (1, 4), (4, 5)]
vertices = ['a', 'b', 'c', 'd', 'e', 'f']
graph = Graph(edges, vertices)
print('\n        Calculate Distance (0, 4):', graph.calc_distance(0, 4))  # 2
assert graph.calc_distance(0, 4) == 2, "calc_distance() should be 2, but was {}".format(graph.calc_distance(0, 4))
print('        Calculate Distance (5, 2):', graph.calc_distance(5, 2))  # 3
assert graph.calc_distance(5, 2) == 3, "calc_distance() should be 3, but was {}".format(graph.calc_distance(5, 2))
print('        Calculate Distance (0, 5):', graph.calc_distance(0, 5))  # 3
assert graph.calc_distance(0, 5) == 3, "calc_distance() should be 3, but was {}".format(graph.calc_distance(0, 5))
print('        Calculate Distance (4, 1):', graph.calc_distance(4, 1))  # 1
assert graph.calc_distance(4, 1) == 1, "calc_distance() should be 1, but was {}".format(graph.calc_distance(4, 1))
print('        Calculate Distance (3, 3):', graph.calc_distance(3, 3))  # 0
assert graph.calc_distance(3, 3) == 0, "calc_distance() should be 0, but was {}".format(graph.calc_distance(3, 3))
print('\n    Calculate Distance Tests PASS!!!')

print('\n    Calculate Shortest Distance tests...')
edges = [(0, 1), (1, 2), (1, 3), (3, 4), (1, 4), (4, 5)]
vertices = ['a', 'b', 'c', 'd', 'e', 'f']
graph = Graph(edges, vertices)
print('\n        Calculate Shortest Distance (0, 4):', graph.calc_shortest_path(0, 4))  # [0, 1, 4]
assert graph.calc_shortest_path(0, 4) == [0, 1, 4], "calc_shortest_path() should be [0, 1, 4], but was {}".format(graph.calc_shortest_path(0, 4))
print('        Calculate Shortest Distance (5, 2):', graph.calc_shortest_path(5, 2))  # [5, 4, 1, 2]
assert graph.calc_shortest_path(5, 2) == [5, 4, 1, 2], "calc_shortest_path() should be [5, 4, 1, 2], but was {}".format(graph.calc_shortest_path(5, 2))
print('        Calculate Shortest Distance (0, 5):', graph.calc_shortest_path(0, 5))  # [0, 1, 4, 5]
assert graph.calc_shortest_path(0, 5) == [0, 1, 4, 5], "calc_shortest_path() should be [0, 1, 4, 5], but was {}".format(graph.calc_shortest_path(0, 5))
print('        Calculate Shortest Distance (4, 1):', graph.calc_shortest_path(4, 1))  # [4, 1]
assert graph.calc_shortest_path(4, 1) == [4, 1], "calc_shortest_path() should be [4, 1], but was {}".format(graph.calc_shortest_path(4, 1))
print('        Calculate Shortest Distance (3, 3):', graph.calc_shortest_path(3, 3))  # [3]
assert graph.calc_shortest_path(3, 3) == [3], "calc_shortest_path() should be [3], but was {}".format(graph.calc_shortest_path(3, 3))
print('\n    Calculate Shortest Distance Tests PASS!!!')


print('\nAll Tests PASS!!!')
