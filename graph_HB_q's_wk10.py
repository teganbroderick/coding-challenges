""" Challenge 1: Create a Graph class. Graph instances should store all nodes in a graph. 
It should also have an instance method that adds a Node to the graph and a method that 
connects two existing Node instances together.
"""

class Graph():
    """a graph class"""
    def __init__(self):
        self.nodes = set()

    def add_node(self, node):
        """add node to graph"""
        self.nodes.add(node)

    def connect_nodes(self, node1, node2):
        """connect two nodes together"""
        node1.adjacent.add(node2)
        node2.adjacent.add(node1)

class Node:
    """A graph node."""

    def __init__(self, data, adjacent=None):
        self.data = data
        self.adjacent = adjacent or set()

""" Challenge 2: Write a function that takes in a Node object and prints all connected nodes."""

def connect_nodes(node):
    """print nodes connected to input node"""

    seen_nodes = set()
    nodes_to_check = [node]

    while nodes_to_check != []:
        current = nodes_to_check.pop()
        adj_nodes = current.adjacent
        
        for adj_node in adj_nodes:
            if adj_node not in seen_nodes:
                seen_nodes.add(adj_node)
                nodes_to_check.append(node)


"""
Write a function that takes in two Node objects and returns True if the nodes are connected to one another.
"""

def are_nodes_adjacent(node1, node2):
    """return True if nodes are adjacent to one another"""

    seen_set = set()
    nodes_to_check = [node1]

    while nodes_to_check != []:
        current = nodes_to_check.pop()
        adj_nodes = current.adjacent
        for adj_node in adj_nodes:
            if adj_node not in seen_set:
                seen_set.add(adj_node)
                nodes_to_check.append(adj_node)

    if node2 in seen_set:
        return True






