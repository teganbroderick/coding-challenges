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