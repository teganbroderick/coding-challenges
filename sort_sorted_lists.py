def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """
    sorted_list = []
    while a != [] or b != []:
        #if either list is empty
        if a == []:
            sorted_list.append(b[0])
            b.pop(0)
        elif b == []:
            sorted_list.append(a[0])
            a.pop(0)
        #if comparing two lists with indexed values still present
        elif a[0] < b[0]:
            sorted_list.append(a[0])
            a.pop(0)
        elif a[0] > b[0]:
            sorted_list.append(b[0])
            b.pop(0)


    return sorted_list



a = [1, 3, 5, 7]
b = [2, 6, 8, 10]
print(sort_ab(a,b))
c = [4,5,8,9,20,55]
d = [6,10,15,32]
print(sort_ab(c,d))