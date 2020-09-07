class Directed_Node:
    def __init__(self, index):
        self.index = index
        self.value = None
        self.neighbors = []
        self.parents = []
        self.children = []

    def set_value(self, value):
        self.value = value

    def set_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
        neighbor.neighbors.append(self)
        self.children.append(neighbor)
        neighbor.parents.append(self)
