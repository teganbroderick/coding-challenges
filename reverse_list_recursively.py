def reverse_list_recursively_in_place(list1, first = 0, last = -1):
    """reverse list recursively in place"""

    while first  <= len(list1) // 2 - 1: #midpoint
        
        #switch first and last indexes
        new_last_item = list1[0]
        new_first_item = list1[-1]
        list1[0] = new_first_item
        list1[-1] = new_last_item
        # print(list1)
        #redefine first and last indexes
        first = first + 1
        last = last - 1

        return reverse_list_recursively_in_place(list1, first, last)
    # return list1


print(reverse_list_recursively_in_place([1,2,3,4,5]))
