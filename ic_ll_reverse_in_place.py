def reverse(head_of_list):

    # Reverse the linked list in place
    current = head_of_list
    previous = None
    next_node = None
    
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
        
    return previous