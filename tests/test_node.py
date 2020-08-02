import sys
sys.path.append("src")
from node import Node

print('Testing...')

string_node = Node(0)

print('    string_node.index', string_node.index) # 0
assert string_node.index == 0, "string_node's index should be 0 but was {}".format(string_node.index)

string_node.set_value('asdf')

print('    string_node.value', string_node.value) # 'asdf'
assert string_node.value == 'asdf', "string_node's value should be 'asdf' but was {}".format(string_node.value)

print('    string_node.neighbors', string_node.neighbors) # []
assert string_node.neighbors == [], "string_node's neighbors should be [] but was {}".format(string_node.value)

numeric_node = Node(1)
numeric_node.set_value(765)
numeric_node.set_neighbor(string_node)

print('    numeric_node.neighbors[0].value', numeric_node.neighbors[0].value) # 'asdf'
assert numeric_node.neighbors[0].value == 'asdf', "numeric_node's first neighbor should be the node with value 'asdf' but was {}".format(
    string_node.neighbors[0].value)

print('    string_node.neighbors[0].value', string_node.neighbors[0].value) # 765
assert string_node.neighbors[0].value == 765, "string_node's first neighbor should be the node with value 765 but was {}".format(string_node.neighbors[0].value)

array_node = Node(2)
array_node.set_value([[1, 2], [3, 4]])
array_node.set_neighbor(numeric_node)

print('    array_node.neighbors[0].value', array_node.neighbors[0].value)  # 765
assert array_node.neighbors[0].value == 765, "array_node's first neighbor should be the node with value 765 but was {}".format(array_node.neighbors[1].value)

print('    numeric_node.neighbors[1].value', numeric_node.neighbors[1].value) # [[1, 2], [3, 4]]
assert numeric_node.neighbors[1].value == [[1, 2], [3, 4]], "numeric_node's second neighbor should be the node with value [[1, 2], [3, 4]] but was {}".format(numeric_node.neighbors[1].value)

print('ALL Tests PASS!!!')
