def rev_list_in_place(lst):
    """Reverse list in place.

    You cannot do this with reversed(), .reverse(), or list slice
    assignment!
    """

    for i in range(len(lst)//2):
        start = lst[i] #0, 1
        end = lst[-i-1] #-1, -2

        lst[i] = end
        lst[-i-1] = start
    return lst

print(rev_list_in_place([1, 2, 3]))
