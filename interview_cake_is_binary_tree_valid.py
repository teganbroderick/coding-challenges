def is_binary_tree_valid(root):
    """return true if binary tree is valid"""

    #traverse tree
    #depth first
    #everything on the left has to be smaller than root
    #everything on right has to be larger than root
    #keep track of upper and lower bounds for each node, and validate value of node in relation to these values


    to_check = [root, -float(inf), float(inf)]
   
    while to_check != []:
        #pop off values from to check list stack
        current, lower_bound, upper_bound = to_check.pop()
        
        #current needs to be less than upper limit and greater than lower limit
        if current >= upper_bound and current <= lower_bound:
            return False

        if current.left != None:
            to_check.append(current.left, lower_bound, current.value)

        if current.right != None:
            to_check.append(current.right, current.value, upper_bound)

    return True
