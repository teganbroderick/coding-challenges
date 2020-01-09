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

    if 0 not in blueprint[0]:
        return False

    # col = "x"
    # row = "x"

    #find 1st pipe, initiate first position
    for i in range(0, len(blueprint[0])): #traverse across
        if blueprint[0][i] == 0:
            col = i
            row = 0
   
    

    # check to left, right, and down from pipe, if pipe is there, reassign pipe var to it, and keep searching
    while row < len(blueprint):
        if blueprint[row][col - 1] == 0:
            blueprint = [row][col - 1]
            row = row
        elif blueprint[row][col + 1] == 0:
            blueprint = [row][col + 1]
            row = row
        elif blueprint[row + 1][col] == 0:
            print("row top", row + 1)
            if row + 1 == len(blueprint):
                print("row if", row + 1)
                return True
            else:
                print("row else", row + 1)
                blueprint = [row + 1][col]
                row = row + 1
        else:
            return False

    return True

print(can_water_flow([[1, 0, 1],[1, 0, 1],[1, 0, 1]]))


