class Node:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""
        
        self.data = data
        self.left = left
        self.right = right
        
    def is_valid(self, upper_limit = float('inf'), lower_limit = -float('inf')):
        """Is this tree a valid BST?"""
        
        if self.data > upper_limit or self.data < lower_limit:
            return False
        
        if self.left != None:
            return Node.is_valid(self.left, upper_limit, self.data)

        if self.right != None:
            return Node.is_valid(self.right, self.data, lower_limit)

        return True

t = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
print(t.is_valid())

t = Node(4, Node(2, Node(3), Node(3)), Node(6, Node(5), Node(7)))
print(t.is_valid())