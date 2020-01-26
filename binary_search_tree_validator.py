class Node:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""
        
        self.data = data
        self.left = left
        self.right = right
        
    # def is_valid_using_recursion(self, upper_limit = float('inf'), lower_limit = -float('inf')):
    #     """Is this tree a valid BST?"""
        
    #     if self.data > upper_limit or self.data < lower_limit:
    #         return False
        
    #     if self.left != None:
    #         return Node.is_valid(self.left, upper_limit, self.data)

    #     if self.right != None:
    #         return Node.is_valid(self.right, self.data, lower_limit)

    #     return True

    def is_valid(self):
        """Is this tree a valid BST?"""
        
        to_check = [(self, -float("inf"), float("inf"))]

        while to_check != []:
            node, lower_limit, upper_limit = to_check.pop()

            if node.data >= upper_limit or node.data <= lower_limit:
                return False

            if node.left != None:
                #This node must be less than the current node, so set upper limit to value of current node
                to_check.append((node.left, lower_limit, node.data))

            if node.right != None:
                #This node must be greater than the current node, so set lower limit to value of current node
                to_check.append((node.right, node.data, upper_limit))

        return True

        

t = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
print(t.is_valid())

t = Node(4, Node(2, Node(3), Node(3)), Node(6, Node(5), Node(7)))
print(t.is_valid())