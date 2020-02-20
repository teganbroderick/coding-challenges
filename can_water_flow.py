"""
Pipe blueprints are encoded as 2-dimensional matrices. Here’s an example of a valid blueprint:

1 0 1 1
1 0 1 1
1 0 0 0
1 1 1 0

1 1   This blueprint doesn't have any pipes
1 1

1 1 1   <- No place for water to start flowing
1 0 1
1 0 1

0 1 1
1 0 1   <- Water can't flow diagonally
1 0 1

"""


def can_water_flow(blueprint):
    """Return True if water can flow through the blueprint."""

#find 0 in row 1, assign position to current
#check left, right, down for next 0
#if 0 exists, reassign current to that position
#keep going until current is in the bottom row (len(grid))

    if 0 not in blueprint[0]:
        return False

    # print("length blueprint", len(blueprint))
    # print("length blueprint rows", len(blueprint[0]))

    for i in range(len(blueprint[0])-1):
        if blueprint[0][i] == 0:
            row = 0
            col = i
            # print("original position", row, col)

            seen_list = [(row, col)]

    while row < (len(blueprint) - 1):
        #check left
        if col != 0 and (row, col-1) not in seen_list and blueprint[row][col-1] == 0:
            row = row
            col -= 1
            seen_list.append((row, col))
            # print("moved left", row, col)
        
        #check right
        elif col != (len(blueprint[0]) -1) and blueprint[row][col + 1] == 0 and (row, col+1) not in seen_list:
            row = row
            col += 1
            seen_list.append((row, col))
            # print("moved right", row, col)
        
        #check down
        elif blueprint[row+1][col] == 0:
            row += 1
            col = col       
            seen_list.append((row, col))
            # print("moved down", row, col)    
        
        #if there is no 0 left, right or down, return False
        else:
            return False
    
    return True

print(can_water_flow([  [1, 0, 1],
                        [0, 0, 1],
                        [0, 1, 1],
                        [0, 1, 1]]))


# good_blueprint = [  [1, 0, 0, 0, 1, 1],
#                     [1, 0, 1, 0, 0, 1],
#                     [1, 1, 0, 0, 0, 0],
#                     [1, 1, 0, 1, 1, 1],]

# print(can_water_flow(good_blueprint))


