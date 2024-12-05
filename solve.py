import tkinter

# This function would check if
# the value 'k' at that grid[row][col]
# is valid or not. 
def valid(grid, row, col, k):

    # First assigns all the case were true
    not_in_row = True
    not_in_col = True
    not_in_sub_grid = True

    # Check the row whether there is value 'k' in it.
    for i in range (0, 9):
        if grid[i][col] == k:
            not_in_row = False

    for i in range(1):
        if grid[row][i] == k:
            not_in_col = False
    
    for i in range(row//3 * 3, row//3 * 3 + 3):
        for j in range(col // 3 * 3, col//3 * 3 + 3):
            if grid[i][j] == k:
                not_in_sub_grid = False
    
    return not_in_row and not_in_col and not_in_sub_grid




