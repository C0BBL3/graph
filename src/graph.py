class Graph:
    def __init__(self, edges, vertices):
        self.edges = edges
        self.vertices = vertices
        self.make_nodes()

    def make_nodes(self):
        uncorrected_edges = [i for edge in self.edges for i in edge]

        corrected_edges = self.remove_duplicate_edges(uncorrected_edges)  # no more duplicates

        # make the nodes (but without values or neighbors)
        self.nodes = [Node(i) for i in corrected_edges]

        for i, node in enumerate(self.nodes):  # give the nodes their values
            node.set_value(self.vertices[i])

        for x, y in self.edges:  # give the nodes their neighbors
            self.nodes[x].set_neighbor(self.nodes[y])

    def remove_duplicate_edges(self, edges):
        corrected_edges = []
        for edge in edges:
            if edge not in corrected_edges:
                corrected_edges.append(edge)

        return corrected_edges

    def depth_first_search(self, index, visited_nodes=[]):
        un_visited_neighbors = []

        if self.nodes[index] not in visited_nodes:
            visited_nodes.append(self.nodes[index])

        for neighbor in self.nodes[index].neighbors:
            if neighbor not in visited_nodes:
                un_visited_neighbors.append(neighbor)

        if un_visited_neighbors != []:
            for node in un_visited_neighbors:
                self.depth_first_search(node.index, visited_nodes)

        return [node.index for node in visited_nodes]

    def breadth_first_search(self, index, index_2=None):
        visited_nodes, queue = [], [self.nodes[index]]

        while len(visited_nodes) < len(self.nodes):

            for neighbor in queue[0].neighbors:
                queue.append(neighbor)

            if queue[0] not in visited_nodes:
                visited_nodes.append(queue[0].index)

            queue.remove(queue[0])

        return visited_nodes

    def calc_distance(self, node_1_index, node_2_index):
        generation_number, current_generation_nodes, visited_nodes, previous_generation_nodes = 0, [], [self.nodes[node_1_index]], [self.nodes[node_1_index]]
        if node_1_index == node_2_index:
            return 0
        while True:
            generation_number += 1
            for node in previous_generation_nodes:
                for neighbor in node.neighbors:
                    if neighbor not in visited_nodes:
                        neighbor.previous = node
                    visited_nodes.append(neighbor)
                    current_generation_nodes.append(neighbor)
            if self.nodes[node_2_index] in current_generation_nodes:
                return generation_number

            
            previous_generation_nodes = current_generation_nodes
            current_generation_nodes = []

    def calc_shortest_path(self, node_1_index, node_2_index):
        distance, shortest_path, current_node = self.calc_distance(node_1_index, node_2_index), [self.nodes[node_2_index].index], self.nodes[node_2_index]
        while len(shortest_path) < distance + 1:
            if current_node.previous != None:
                shortest_path.append(current_node.previous.index)
                current_node = current_node.previous
        for node in self.nodes: node.previous = None #reset all the previous attributes so no error for next tests
        return shortest_path[::-1]

class Node:
    def __init__(self, index):
        self.index = index
        self.value = None
        self.neighbors = []
        self.parent = None

    def set_value(self, value):
        self.value = value

    def set_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
        neighbor.neighbors.append(self)

            

        
