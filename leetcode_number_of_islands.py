"""Traverse 2D matrix, and return number of islands. Land is 
represented by "1" and water is represented by "0". Islands are formed
by 1s connected horizontally and vertically"""

#traverse matrix
#if val is 1,  
    #add 1 to count
    #pass position in matrix through to check_adj function
    #zero out current position, and check adjacent cells to see if they are also contain
    #recursively call check_adj function until all adjacent 1 cells have been zeroed out


def numIslands(grid):
    
    if grid == []:
        return 0
    
    row = len(grid)
    col = len(grid[0])
    count = 0
    
    for i in range(row):     
        for j in range(col):
            if grid[i][j] == "1":
                count += 1
                check_adj(grid, row, col, i, j)

    return count

def check_adj(self, grid, row, col, i, j):
    #zero out 1
    grid[i][j] = "0"
    
    #check up
    if i != 0 and grid[i-1][j] == "1": 
        check_adj(grid, row, col, i-1, j)
    #check down
    if i != row-1 and grid[i+1][j] == "1": 
        check_adj(grid, row, col, i+1, j)
    #check left
    if j != 0 and grid[i][j-1] == "1":
        check_adj(grid, row, col, i, j-1)
    #check right
    if j != col-1 and grid[i][j+1] == "1": 
        check_adj(grid, row, col, i, j+1)
    #if nothing left to check, return
    return 
    
