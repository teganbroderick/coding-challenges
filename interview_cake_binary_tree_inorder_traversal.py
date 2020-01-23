def inorder_traversal(node):
    """print in order traversal of binary tree"""

    if node != None:
        #items in left tree are less than node, so print that recursively first
        inorder_traversal(node.left)
        #print node
        print(node.value)
        #items in right tree are greater than node, so print that recursively second
        inorder_traversal(node.right)
