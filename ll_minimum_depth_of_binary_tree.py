def minDepth(root_node):
    #num of nodes along the shortest path form the 
    #root node down to the nearest left node
    
    #start at root node
    #traverse tree
    #keep track of layers in tree

    to_check = [root_node]
    seen_list = [root_node]

    while to_check != []:
        current = to_check.pop(0)
        if current.left != None:
            to_check.append(current.left)
            seen_list.append(current.left)
        if current.right != None:
            to_check.append(current.right)
            seen_list.append(current.right)


