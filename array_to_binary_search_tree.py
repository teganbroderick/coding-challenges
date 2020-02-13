#in => sorted array
#out => balanced binary search tree made from array elements

def array_to_BST(node_list):
    """return BST made from elements of node_list"""
    #base case - return if slice is an empty list
    #find midpoint of array
    #make midpoint root node
    #recursively call function on everything to the left of the root node
    #recursively call function on everything to the right of the root node
    #return root
    
    if node_list == []:
        return

    midpoint = len(node_list) // 2
    root = node_list[midpoint]

    node.left = array_to_BST(node_list[0:midpoint])
    node.right = array_to_BST(node_list[midpoint+1:])

    return root