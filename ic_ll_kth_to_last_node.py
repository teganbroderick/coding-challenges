def kth_to_last_node(k, head):

    # Return the kth to last node in the linked list
    
    #traverse whole ll, get length
    current = head
    count = 0
    while current:
        count += 1
        current = current.next
        
    #if k is greater than length of list, can't get kth to last node
    if k > count:
        return None

    #traverse ll again, stopping at count-k
    #this is the kth to last node
    current = head
    for i in range(0, count-k):
        current = current.next
    
    return current