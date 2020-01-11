def spiral(matrix_size):
    """Spiral coordinates of a matrix of `matrix_size` size."""

    #make matrix
    nested_list = []
    for i in range(matrix_size):
        interior_list = []
        for j in range(matrix_size):
            interior_list.append("x")
        nested_list.append(interior_list)
    print(nested_list)

    #traverse matrix


spiral(4)

def spiral_by_nested_boxes(matrix_size):
    """Spiral coordinates of a matrix of `matrix_size` size.

    This version works by drawing TRBL boxes until the entire matrix
    has been printed.
    """

    # Loop and create square nested boxes

    for box_number in range(0, matrix_size // 2):
        top = left = box_number
        bottom = right = matrix_size - box_number - 1

        for x in range(left, right):  # draw top line going >
            print((x, top))

        for y in range(top, bottom):  # draw right line going \/
            print((right, y))

        for x in range(right, left, -1):  # draw bottom line going <
            print((x, bottom))

        for y in range(bottom, top, -1):  # draw left line going /\
            print((left, y))

    # Odd-width matrices: print center point manually

    if matrix_size % 2 != 0:
        print((matrix_size // 2, matrix_size // 2))

spiral_by_nested_boxes(4)