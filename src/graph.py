from node import Node


class Graph:
    def __init__(self, edges, vertices):
        self.edges = edges
        self.vertices = vertices
        self.make_nodes()

    def make_nodes(self):
        uncorrected_edges = [i for edge in self.edges for i in edge]

        corrected_edges = self.remove_duplicate_edges(
            uncorrected_edges)  # no more duplicates

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

    def breadth_first_search(self, index, index_2=None, return_distance=False):
        distance, visited_nodes, queue = 0, [], [self.nodes[index]]

        if return_distance and index == index_2:
            return 0

        while len(visited_nodes) < len(self.nodes):
            
            for neighbor in queue[0].neighbors:
                queue.append(neighbor)

            

            if queue[0] not in visited_nodes:
                visited_nodes.append(queue[0].index)

            queue.remove(queue[0])

            distance += 1

            if return_distance == True:

                if self.nodes[index_2] in queue:
                    return distance

        return visited_nodes

    def find_distance(self, node_1_index, node_2_index):
        return_1_2 = self.breadth_first_search(node_1_index, index_2=node_2_index, return_distance=True)
        print(return_1_2)
        return_2_1 = self.breadth_first_search(node_2_index, index_2=node_1_index, return_distance=True)
        print(return_2_1)
        if return_1_2 < return_2_1:
            return return_1_2
        else:
            return return_2_1





