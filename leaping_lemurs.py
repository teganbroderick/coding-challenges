#A lemur wants to jump across a span in the forest on branches. 
#She can jump 1 or 2 branches at a time. 
#Unfortunately, some of the branches are on dead trees, and she can’t use those branches to jump.

def how_many_leaps(branch_list):
    """return how many leaps needed to cross branch list"""

    if len(branch_list) == 1:
        return 0
    
    count = 0
    while branch_list != []:
        if len(branch_list) >= 3:
            if branch_list[2] == 0:
                count += 1
                # print(count)
                branch_list.pop(0)
                branch_list.pop(0)
            elif branch_list[2] != 0:
                count += 1
                # print(count)
                branch_list.pop(0)
        else:
            if len(branch_list) == 1:
                branch_list.pop(0)
            elif len(branch_list) == 2:
                count += 1
                branch_list.pop(0)
                branch_list.pop(0)

    return count


print(how_many_leaps([0, 0]))
print(how_many_leaps([0, 1, 0]))
print(how_many_leaps([0, 0, 1, 0]))
print(how_many_leaps([0, 0, 0, 0, 1, 0, 0, 1, 0]))