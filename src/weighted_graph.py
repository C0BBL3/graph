class WeightedGraph:
    def __init__(self, weights, vertex_values):
        self.weights = weights
        self.nodes = [WeightedNode(index, value) for index, value in enumerate(vertex_values)]
        self.make_nodes()

    def make_nodes(self):
        for neighbors, weight in self.weights.items():
            self.nodes[neighbors[0]].set_neighbor(self.nodes[neighbors[1]])
            self.nodes[neighbors[0]].set_neighbor_weights(self.nodes[neighbors[1]], weight)

    def calc_shortest_path(self, start_index, end_index):
        if start_index == end_index:
            return [self.nodes[start_index]]
        else:
            self.tentative_distances = [10000000000 if node.index != start_index else 0 for node in self.nodes]
            self.set_distance_values(self.nodes[start_index], start_index, end_index, unvisited_nodes=[node for node in self.nodes])
            current_node = self.nodes[end_index]
            unvisited_nodes = [node for node in self.nodes]
            while current_node.index != start_index:    
                current_node_neighbors = [node.index for node in self.nodes if node.index in current_node.neighbors.keys()]
                old_current_node = current_node
                neighbor_tentative_distances = []
                for index, node in enumerate(self.nodes):
                    if index in current_node_neighbors and self.nodes[index] in unvisited_nodes:
                        neighbor_tentative_distances.append((index, self.tentative_distances[index] + current_node.neighbor_weights[index]))
                current_node = self.nodes[min(neighbor_tentative_distances, key=lambda x: x[1])[0]]
                old_current_node.set_parent(current_node)
                unvisited_nodes.remove(old_current_node)
            path = self.get_path(self.nodes[start_index], self.nodes[end_index])
            return path
    
    def set_distance_values(self, current_node, start_index, end_index, unvisited_nodes = None):
        current_node_neighbors = [node for node in self.nodes if node.index in current_node.neighbors.keys()]
        for node in current_node_neighbors:
            distance = self.tentative_distances[current_node.index] + current_node.neighbor_weights[node.index]
            if distance < self.tentative_distances[node.index]:
                self.tentative_distances[node.index] = distance
                self.set_distance_values(node, start_index, end_index, unvisited_nodes = unvisited_nodes)
        
    def get_path(self, current_node, end_node, nodes = None):
        if nodes is None: nodes = []
        if current_node is not end_node:
            nodes.append(current_node)
            return self.get_path(current_node.child, end_node, nodes=nodes)
        else:
            nodes.append(current_node)
            return nodes

class WeightedNode:
    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.neighbors = {}
        self.neighbor_weights = {}
        self.parent = None
        self.neighbor_tentative_distances = {}

    def set_neighbor(self, neighbor):
        if self not in neighbor.neighbors:
            self.neighbors[neighbor.index] = neighbor
        if self not in neighbor.neighbors:
            neighbor.neighbors[self.index] = self

    def set_neighbor_weights(self, neighbor, weight):
        if neighbor.index not in self.neighbor_weights.keys():
            self.neighbor_weights[neighbor.index] = weight
        if self.index not in neighbor.neighbor_weights.keys():
            neighbor.neighbor_weights[self.index] = weight

    def set_child(self, child):
        self.child = child
        child.parent = self

    def set_parent(self, parent):
        self.parent = parent
        parent.child = self