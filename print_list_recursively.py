#print list using recursion

def print_list(list1):
    """print list using recursion"""

    while list1 != []:
        print(list1[0])
        list1.pop(0)
        
        print_list(list1)

print_list([1, 2, 3])
