import sys
sys.path.append("src")
from directed_graph import Directed_Graph

print('\nTesting...\n')

edges = [(0, 1), (1, 2), (3, 1), (4, 3), (1, 4), (4, 5), (3, 6)]
directed_graph = Directed_Graph(edges)

print('        Childs', [[child.index for child in node.children] for node in directed_graph.nodes])
assert [[child.index for child in node.children] for node in directed_graph.nodes] == [[1], [2, 4], [], [1, 6], [3, 5], [], []], "Childs was wrong it should be [[1], [2, 4], [], [1, 6], [3, 5], []], but was {}".format([[child.index for child in node.children] for node in directed_graph.nodes])
print('        Childs Passed!!!\n')

print('        Parents', [[parent.index for parent in node.parents] for node in directed_graph.nodes])
assert [[parent.index for parent in node.parents] for node in directed_graph.nodes] == [[], [0, 3], [1], [4], [1], [4], [3]], "Parents was wrong it should be [[], [0, 3], [1], [4], [1], [4], [3]], but was {}".format([[parent.index for parent in node.parents] for node in directed_graph.nodes])
print('        Parents Passed!!!\n')

print('\n    Calculate Distance tests...')
edges = [(0, 1), (1, 2), (3, 1), (4, 3), (1, 4), (4, 5), (3, 6)]
directed_graph = Directed_Graph(edges)
print('\n        Calculate Distance (0, 3):', directed_graph.calc_distance(0, 3))  # 3
assert directed_graph.calc_distance(0, 3) == 3, "calc_distance() should be 3, but was {}".format(directed_graph.calc_distance(0, 3))
print('        Calculate Distance (5, 2):', directed_graph.calc_distance(3, 5))  # 3
assert directed_graph.calc_distance(3, 5) == 3, "calc_distance() should be 3, but was {}".format(directed_graph.calc_distance(3, 5))
print('        Calculate Distance (0, 5):', directed_graph.calc_distance(0, 5))  # 3
assert directed_graph.calc_distance(0, 5) == 3, "calc_distance() should be 3, but was {}".format(directed_graph.calc_distance(0, 5))
print('        Calculate Distance (4, 1):', directed_graph.calc_distance(4, 1))  # 2
assert directed_graph.calc_distance(4, 1) == 2, "calc_distance() should be 1, but was {}".format(directed_graph.calc_distance(4, 1))
print('        Calculate Distance (3, 3):', directed_graph.calc_distance(2, 4))  # false
assert directed_graph.calc_distance(2, 4) == False, "calc_distance() should be False, but was {}".format(directed_graph.calc_distance(2, 4))
print('\n    Calculate Distance Tests PASS!!!')

print('\n    Calculate Shortest Distance tests...')
edges = [(0, 1), (1, 2), (3, 1), (4, 3), (1, 4), (4, 5), (3, 6)]
directed_graph = Directed_Graph(edges)
print('\n        Calculate Shortest Distance (0, 3):', directed_graph.calc_shortest_path(0, 3))  # [0, 1, 4, 3]
assert directed_graph.calc_shortest_path(0, 3) == [0, 1, 4, 3], "calc_shortest_path() should be [0, 1, 4, 3], but was {}".format(directed_graph.calc_shortest_path(0, 4))
print('        Calculate Shortest Distance (3, 5):', directed_graph.calc_shortest_path(3, 5))  # [3, 1, 4, 5]
assert directed_graph.calc_shortest_path(3, 5) == [3, 1, 4, 5], "calc_shortest_path() should be [3, 1, 4, 5], but was {}".format(directed_graph.calc_shortest_path(5, 2))
print('        Calculate Shortest Distance (0, 5):', directed_graph.calc_shortest_path(0, 5))  # [0, 1, 4, 5]
assert directed_graph.calc_shortest_path(0, 5) == [0, 1, 4, 5], "calc_shortest_path() should be [0, 1, 4, 5], but was {}".format(directed_graph.calc_shortest_path(0, 5))
print('        Calculate Shortest Distance (4, 1):', directed_graph.calc_shortest_path(4, 1))  # [4, 3, 1]
assert directed_graph.calc_shortest_path(4, 1) == [4, 3, 1], "calc_shortest_path() should be [4, 3, 1], but was {}".format(directed_graph.calc_shortest_path(4, 1))
print('        Calculate Shortest Distance (3, 3):', directed_graph.calc_shortest_path(3, 3))  # False
assert directed_graph.calc_shortest_path(3, 3) == False, "calc_shortest_path() should be False, but was {}".format(directed_graph.calc_shortest_path(3, 3))
print('\n    Calculate Shortest Distance Tests PASS!!!')


print('\nAll Tests PASS!!!')
