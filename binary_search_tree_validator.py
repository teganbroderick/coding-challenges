class Node:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""
        
        self.data = data
        self.left = left
        self.right = right
        
    def is_valid(self):
        """Is this tree a valid BST?"""
        
        if self.left.data < self.data and self.right.data > self.data:
            self.left.is_valid()
            self.right.is_valid()
        else:
            return False
        
        return True

t = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
t.is_valid()
