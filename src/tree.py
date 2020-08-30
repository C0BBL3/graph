class Tree:
    def __init__(self, head_value = None):
        self.root = None

    #main functions
    def build_from_edges(self, edges):
        self.set_root(edges)
        layer_nodes = [self.root]
        self.set_children(self.root, edges)

        while len(layer_nodes) > 0:
            next_layer_nodes = self.get_children_of_layer(layer_nodes)
            self.set_children_of_layer(next_layer_nodes)
            layer_nodes = next_layer_nodes

    def print_depth_first(self, node):#must run an initialization function before this (append or build_from_edges)
        print(node.data)
        for child in node.children:
            self.print_depth_first(child)

    def insert(self, tree, node):
        tree.root.parent = node
     
    def print_breadth_first(self, queue = []):
        string = ''
        max_num = 0
        for i in range(0, len(queue)):
            max_num = i
            string += str(queue[i].data) + ' '
        children_arr = []
        for parent in queue:
            for child in parent.children:
                children_arr.append(child)
        for child in children_arr:
            if child != None:
                queue.append(child)
        if len(queue) > 0:
            for i in range(0, max_num + 1):
                queue = queue[:1]
            return self.print_breadth_first(queue)

    #helper functions
    def get_children_of_layer(self, layer_nodes, edges):
        children_of_layer_nodes = []
        for parent in layer_nodes:
            for child in parent.children:
                children_of_layer_nodes.append(child)
        return children_of_layer_nodes

    def set_children_of_layer(self, layer_nodes, edges):
        for node in layer_nodes:
            self.set_children(node, edges)

    def set_root(self, edges):
        [parents, children] = self.set_parent_and_child_lists(edges)
        for i in parents:
            if i not in children:
                self.root = Node(i)

    
    def set_children(self, node, edges):    
        children_from_edges = self.get_children(node, edges)
        for child in children_from_edges:
            if child not in node.children:
                node.children.append(child)

    def get_children(self, node, edges):
        children = []
        for (parent_value, child_value) in edges:
            if parent_value == node.data:
                children.append(Node(child_value))

        return children

    def set_parent_and_child_lists(self, edges):
        parents = []
        children = []
        for arr in edges:
            parents.append(arr[0])
            children.append(arr[1])

        return parents, children #returns a tuple so no one can change it by accident

class Node:
    def __init__(self, value):
        self.data = value
        self.children = []
        self.parent = None

    def children_are_filled(self):
        return self.len_of_child == 2

    def len_of_child(self):
        return len(self.children)
    
    def set_new_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)
