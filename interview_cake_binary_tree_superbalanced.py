def is_binary_tree_super_balanced(root):
    """return true if difference between depth of leafnodes is 1 or less"""

    #traverse tree, DFS
    nodes_to_check = [(root, 0)]

    depth_list = []

    while to_check != []:
        current, depth = nodes_to_check.pop()
        #found leaf
        if current.left == None and current.right == None:
            if depth not in depth_list:
                depth_list.append(depth)
        #not a leaf
        else:
            if current.right != None:
                nodes_to_check.append((current.right, depth+1))     
            elif current.left != None:
                nodes_to_check.append((current.left, depth+1))   

    if depth_list > 2:
        return False
    elif depth_list[1] - depth_list[0] > 1:
        return False
    else:
        return True

