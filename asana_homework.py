
def find_center_of_matrix(matrix):
    """Find center of a 2D matrix. 
    If exact center does not exist, center is square 
    closest to the center with the highest count.
    """

    #find center of columns
    center_column = None
    center_column2 = None
    center_column_odd = None

    #if num columns is even
    if len(matrix[0]) % 2 == 0:
        center_column = len(matrix[0])//2 - 1
        center_column2 = len(matrix[0])//2
    #if num columns is odd
    else: 
        center_column_odd = len(matrix[0])//2
    
    #find center of rows
    center_row = None
    center_row2 = None
    center_row_odd = None
    
    #if num rows is even
    if len(matrix) % 2 == 0:
        center_row = len(matrix)//2 - 1
        center_row2 = len(matrix)//2 - 1
    else:
        #if num columns is odd
        center_row_odd = len(matrix)//2
    
    #find center
    #if there is an exact center
    if center_column_odd != None and center_row_odd != None:
        # print("exact center")
        starting_point = matrix[center_row_odd][center_column_odd]
        col = center_column_odd
        row = center_row_odd

    #if num rows is odd, but num columns is even
    elif center_row_odd != None and center_column != None and center_column2 != None:
        # print("odd num of rows")
        #find larger number in matrix
        starting_point1 = matrix[center_row_odd][center_column]
        starting_point2 = matrix[center_row_odd][center_column2]

        if starting_point1 > starting_point2:
            starting_point = starting_point1
            col = center_column
            row = center_row_odd
        else:
            starting_point = starting_point2
            col = center_column2
            row = center_row_odd
    
    #if num columns is odd, but num rows is even
    elif center_column_odd != None and center_row != None and center_row2 != None:
        # print("odd num of cols")
        #find larger number in matrix
        starting_point1 = matrix[center_row][center_column_odd]
        starting_point2 = matrix[center_row2][center_column_odd]

        if starting_point1 > starting_point2:
            starting_point = starting_point1
            col = center_column_odd
            row = center_row
        else:
            starting_point = starting_point2
            col = center_column_odd
            row = center_row2            

    #if num rows is even and num columns is even 
    elif center_column != None and center_column2 != None and center_row != None and center_row2 != None:
        # print("odd num of rows and cols")
        starting_point1 = matrix[center_row][center_column]
        starting_point2 = matrix[center_row][center_column2]
        starting_point3 = matrix[center_row2][center_column]
        starting_point4 = matrix[center_row2][center_column2]

        if starting_point1 > starting_point2 and starting_point1 > starting_point3 and starting_point1 > starting_point4:
            starting_point = starting_point1
            col = center_column
            row = center_row
        elif starting_point2 > starting_point1 and starting_point2 > starting_point3 and starting_point2 > starting_point4:
            starting_point = starting_point2
            col = center_column2
            row = center_row        
        elif starting_point3 > starting_point1 and starting_point3 > starting_point2 and starting_point3 > starting_point4:
            starting_point = starting_point3
            col = center_column
            row = center_row2   
        elif starting_point4 > starting_point1 and starting_point4 > starting_point2 and starting_point4 > starting_point3:
            starting_point = starting_point4
            col = center_column2
            row = center_row2     

    return (row, col)

def how_many_carrots_eaten(matrix):
    """return how many carrots are eaten by the rabbit in a 2D matrix"""
    
    starting_point = find_center_of_matrix(matrix)
    # print("starting_point", starting_point)
    row = starting_point[0]
    col = starting_point[1]

    #init carrot_count
    carrot_count = 0
    
    #init squares visited
    squares_visited = []
    
    #start with current at starting point
    current = matrix[row][col]
    
    while current!= 0:
        carrot_count += matrix[row][col]
        # print(carrot_count)
        squares_visited.append((row,col))
        # print(squares_visited)

        #check adjacent squares, see if they exist and if they have been visited
        #if they exist and have not been visited, add to dictionary
        #dict key is value at square, dict value is (row, col) tuple
        compare_adj_squares_dict = {}
        #up
        if row != 0 and (row-1,col) not in squares_visited:
            adj_square_up = matrix[row-1][col]
            compare_adj_squares_dict[matrix[row-1][col]] = (row-1, col)
        #down
        if row != (len(matrix) -1) and (row+1,col) not in squares_visited:
            adj_square_down = matrix[row+1][col]
            compare_adj_squares_dict[matrix[row+1][col]] = (row+1, col)
        #left
        if col != 0 and (row,col-1) not in squares_visited:
            adj_square_left = matrix[row][col-1]
            compare_adj_squares_dict[matrix[row][col-1]] = (row, col-1)
        #right
        if col != len(matrix[0]) and (row,col+1) not in squares_visited:
            adj_square_right = matrix[row][col+1]
            compare_adj_squares_dict[matrix[row][col+1]] = (row, col+1)
        # print(compare_adj_squares_dict)
        
        #find square with max value in dict
        sorted_val_list = []
        for key,value in sorted(compare_adj_squares_dict.items()):
            sorted_val_list.append((key,value))
        # print(sorted_val_list)

        max_val = sorted_val_list[-1][0]
        row = sorted_val_list[-1][1][0]
        col = sorted_val_list[-1][1][1]
        current = matrix[row][col]
        
    #return carrot count
    # print("final carrot count", carrot_count)
    return carrot_count

#Code for testing
rabbit_matrix =     [[5, 7, 8, 6, 3],
                    [2, 4, 7, 1, 4],
                    [4, 6, 3, 4, 9],
                    [3, 1, 6, 5, 8]]

rabbit_matrix_zeroed = [[0, 0, 0, 0, 0],
                    [0, 0, 2, 0, 0],
                    [2, 6, 3, 4, 0],
                    [0, 0, 0, 0, 0]]

print(how_many_carrots_eaten(rabbit_matrix))
print(how_many_carrots_eaten(rabbit_matrix_zeroed))




