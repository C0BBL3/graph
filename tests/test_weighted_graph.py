import sys
sys.path.append('src')
from weighted_graph import WeightedGraph

weights = {
    (0,1): 3,
    (1,7): 4,
    (7,2): 2,
    (2,5): 1,
    (5,6): 8,
    (0,3): 2,
    (3,2): 6,
    (3,4): 1,
    (4,8): 8,
    (8,0): 4
}
vertex_values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


print('\nTesting...\n')

weighted_graph_1 = WeightedGraph(weights, vertex_values)
shortest_path_1 = weighted_graph_1.calc_shortest_path(8,4)
print("    Testing Weighted Graph 2's calc_shortest_path")
assert [node.index for node in shortest_path_1] == [8, 0, 3, 4], " Weighted Graph 1's calc_shortest_path was not right, it should be [8, 0, 3, 4], but was {}".format([node.index for node in shortest_path_1])
print("    Weighted Graph 1's row_indices Passed!!!\n")

weighted_graph_2 = WeightedGraph(weights, vertex_values)
shortest_path_2 = weighted_graph_2.calc_shortest_path(6,8)
print("    Testing Weighted Graph 2's calc_shortest_path")
assert [node.index for node in shortest_path_2] == [6, 5, 2, 3, 0, 8], " Weighted Graph 2's calc_shortest_path was not right, it should be [6, 5, 2, 3, 0, 8], but was {}".format([node.index for node in shortest_path_2])
print("    Weighted Graph 2's row_indices Passed!!!\n")

weighted_graph_3 = WeightedGraph(weights, vertex_values)
shortest_path_3 = weighted_graph_3.calc_shortest_path(7,4)
print("    Testing Weighted Graph 3's calc_shortest_path")
assert [node.index for node in shortest_path_3] == [7, 2, 3, 4], " Weighted Graph 3's calc_shortest_path was not right, it should be [7, 2, 3, 4], but was {}".format([node.index for node in shortest_path_3])
print("    Weighted Graph 3's row_indices Passed!!!\n")

weighted_graph_4 = WeightedGraph(weights, vertex_values)
shortest_path_4 = weighted_graph_4.calc_shortest_path(8,7)
print("    Testing Weighted Graph 4's calc_shortest_path")
assert [node.index for node in shortest_path_4] == [8, 0, 1, 7], " Weighted Graph 4's calc_shortest_path was not right, it should be [8, 0, 1, 7], but was {}".format([node.index for node in shortest_path_4])
print("    Weighted Graph 4's row_indices Passed!!!\n")

weighted_graph_5 = WeightedGraph(weights, vertex_values)
shortest_path_5 = weighted_graph_5.calc_shortest_path(8,6)
print("    Testing Weighted Graph 5's calc_shortest_path")
assert [node.index for node in shortest_path_5] == [8, 0, 3, 2, 5, 6], " Weighted Graph 5's calc_shortest_path was not right, it should be [8, 0, 3, 2, 5, 6], but was {}".format([node.index for node in shortest_path_5])
print("    Weighted Graph 5's row_indices Passed!!!\n")

print('All Tests PASS!!!')