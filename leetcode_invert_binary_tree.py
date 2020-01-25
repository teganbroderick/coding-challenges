def invertTree(root):
    """invert a binary tree in place"""
    
    #root = root
    #root.left = root.right
    #root.right = root.left
    #and so on
    
    if root == None:
        return None
    
    to_invert = [root]
    
    while to_invert != []:
        current = to_invert.pop()
        #assign nodes to variables
        
        right_node = current.right
        left_node = current.left
        #reassign nodes to opposite sides
        current.right = left_node
        current.left = right_node
        
        if current.left != None:
            to_invert.append(current.left)
        if current.right != None:
            to_invert.append(current.right)
    return root