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
