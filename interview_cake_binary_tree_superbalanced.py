def is_balanced(tree_root):
    """return true if difference between depth of leafnodes is 1 or less"""
    # Determine if the tree is superbalanced
    
    #traverse tree, start at root node
    #keep track of node and depth (tuple)
    #record depths in a list or set
    #record nodes to check in a stack
    
    #once we get to a leaf, node. left == None and node.right == None,
        #put depth in depth list
    #if depth list length ever goes over 2, return False
    #if differences between depths in list are more than one, return False
    
    to_check = [(tree_root, 0)]
    depth_list = []
    
    while to_check:
        current, depth = to_check.pop()
        
        if current.right == None and current.left == None:
            if depth not in depth_list:
                depth_list.append(depth)
        
            if len(depth_list) > 2:
                return False
            elif len(depth_list) == 2:
                if depth_list[1] - depth_list[0] > 1 or depth_list[0] - depth_list[1] > 1:
                    return False

        if current.left != None:
            to_check.append((current.left, depth + 1))
            
        if current.right != None:
            to_check.append((current.right, depth + 1))
        

    return True

