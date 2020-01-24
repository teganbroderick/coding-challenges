def reverse_ll_recursively(head_node, prev = None):
    """reverse linked list recursively"""

    #base case
    #how can we change the state to get close to the base case
    #call the function

    #in: 1 - 2 - 3 - 4 - 5 - Null
    #out: 5 - 4 - 3 - 2 - 1 - Null

    #not recursively: 
    #iterate throught linked list, 
    #save nodes to list, 
    #iterate through list, 
    #pop off last element, add to new ll

    #base_case = node.next == None

    if head_node.next == None or head == None:
        return head_node 

    call = reverse_ll_recursively(head.next) #calls until you reach 5
    
    head.next.next = head
    head.next = None
    return call





