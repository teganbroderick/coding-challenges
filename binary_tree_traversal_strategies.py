class Node:
def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def in_order_traversal(root):
    """traverse a binary tree in order"""

    #left, root, right

    if root != None:
        in_order_traversal(root.left)
        print(root.value)
        in_order_traversal(root.right)
    return

def pre_order_traversal(root):
    """traverse binary tree in pre order"""

    #root, left, right

    if root != None:
        print(root.value)
        in_order_traversal(root.left)
        in_order_traversal(root.right)

def post_order_traversal(root):
    """traverse binary tree in post order"""

    #left, right, root
    if root != None:
        in_order_traversal(root.left)
        in_order_traversal(root.right)
        print(root.value)
