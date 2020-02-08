def contains_cycle(first_node):
    """Check if the linked list contains a cycle"""
    if first_node == None:
        return False
    
    seen_set = set()
    current = first_node
    
    while current:
        if current in seen_set:
            return True
        else:
            seen_set.add(current)
            current = current.next
    
    return False