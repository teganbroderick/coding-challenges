def sum_list_recursively(list1):
    """return sum of list items using recursion"""

    #steps:
    #base case
    #move towards base case
    #call function 

    #base case = empty list

    if list1 == []:
        return 0

    return sum_list_recursively(list1[1:]) + list1[0]

print(sum_list_recursively([-5, 10, 4]))