def reverse_list(list1):
    """reverse list, not in place"""

    new_list = []
    for i in range(len(list1)-1, -1, -1):
        
        new_list.append(list1[i])

    return new_list

print(reverse_list([1,2,3,4,5]))