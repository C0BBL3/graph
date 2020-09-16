from directed_node import Directed_Node


class Directed_Graph:
    def __init__(self, edges, vertices = None):
        self.edges = edges
        self.vertices = vertices
        self.make_nodes()

    def make_nodes(self):
        uncorrected_edges = [i for edge in self.edges for i in edge]

        corrected_edges = self.remove_duplicate_edges(uncorrected_edges)

        self.nodes = [Directed_Node(i) for i in corrected_edges]

        
        for i, node in enumerate(self.nodes):
            if self.vertices != None:
                node.set_value(self.vertices[i])
            else:
                node.set_value(i)

        for x, y in self.edges:
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
        generation_number, current_generation_nodes = 0, []
        visited_nodes = [self.nodes[node_1_index]]
        previous_generation_nodes = [self.nodes[node_1_index]]
        if node_1_index == node_2_index:
            return 0
        while generation_number < len(self.nodes):
            generation_number += 1
            for node in previous_generation_nodes:
                for child in node.children:
                    if child not in visited_nodes:
                        child.previous = node
                    visited_nodes.append(child)
                    current_generation_nodes.append(child)
            if self.nodes[node_2_index] in current_generation_nodes:
                return generation_number
            previous_generation_nodes = current_generation_nodes
            current_generation_nodes = []
        return False

    def calc_shortest_path(self, node_1_index, node_2_index):
        distance,  = self.calc_distance(node_1_index, node_2_index)
        shortest_path = [self.nodes[node_2_index].index]
        current_node = self.nodes[node_2_index]
        if node_1_index == node_2_index:
            return False
        while len(shortest_path) < distance + 1:
            if current_node.previous != None:
                if current_node.previous in current_node.parents:
                    shortest_path.append(current_node.previous.index)
                    current_node = current_node.previous
                else:
                    return False
        for node in self.nodes: node.previous = None #reset all the previous attributes so no error for next tests
        return shortest_path[::-1]
            

        
