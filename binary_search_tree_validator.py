class Node:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""
        
        self.data = data
        self.left = left
        self.right = right
        
    def is_valid(self):
        """Is this tree a valid BST?"""
        print("in function", self.data)
        #while there are nodes to traverse
        if self.left != None or self.right != None:
            #if left node data is less that root, and right node data is greater than root
            if self.left.data < self.data and self.right.data > self.data:
                #conditions satisfied, keep traversing tree
                #run method on left node and right node
                self.left.is_valid()
                self.right.is_valid()
            else:
                #conditions not satisfied, return false
                print("in else conditional", self.data)
                return False
        #tree traversed, conditions met, return true
        return True

t = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
print(t.is_valid())

t = Node(4, Node(2, Node(3), Node(3)), Node(6, Node(5), Node(7)))
print(t.is_valid())