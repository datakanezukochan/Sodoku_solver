import tkinter as tk
from tkinter import messagebox

# Create the Tkinter window
parent = tk.Tk()
parent.title("Sudoku Solver")

# random sudoku I take from the import tkinter as tk
from tkinter import messagebox

# Create the Tkinter window
parent = tk.Tk()
parent.title("Sudoku Solver")

# random sudoku I take from the internet
grid = [[9, 2, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 3, 0, 7, 8, 4, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 9, 0, 0],
        [0, 0, 6, 4, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 9, 6, 0, 2, 0],
        [7, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 8, 0, 3, 9, 7, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0]]

# Create a 9x9 grid of entry widgets
entries = [[None for i in range(9)] for i in range(9)]

for row in range(9):
    for col in range(9):
        # Create an input box for each cell in the Sudoku grid.
        entry = tk.Entry(parent, width = 2, font = ('Arial', 30), justify = 'center')
        entry.grid(row = row, column = col, padx = 5, pady = 5)

        # Pre-filled cells
        if grid[row][col] != 0:
            entry.insert(0, str(grid[row][col]))

            # Make the input box read-only
            entry.config(state = 'disabled')

        entries[row][col] = entry


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

    # Check the column whether there is value 'k' in it.
    for i in range(0, 9):
        if grid[row][i] == k:
            not_in_col = False

    # Check the box (sub grid) whether there is value 'k' in it. 
    for i in range(row//3 * 3, row//3 * 3 + 3):
        for j in range(col // 3 * 3, col//3 * 3 + 3):
            if grid[i][j] == k:
                not_in_sub_grid = False
    
    return not_in_row and not_in_col and not_in_sub_grid


# Backtrack every possible cases for suitable number in the grid
def back_tracking(grid, row = 0, col = 0):
    # Base case
    # If check all the board, return True
    # Which is there is solution for the board
    if row == 9:
        return True
    
    # If the column exceed 9, start checking the next row
    elif col == 9:
        return back_tracking(grid, row + 1, 0)
    
    # If that position is already filled with number,
    # move to the next column 
    elif  grid[row][col] != 0:
        return back_tracking(grid, row, col + 1)

    # When that position is blank,
    # Plug the number in (start from 1)
    # If it's met the condition, check the next position
    # until if it's not met, backtrack to the latest position 
    # and change increase the number by 1 until it suitable the case 

    else:
        # for i in range(1, 10):
        #     if valid(grid, row, col, i):
        #         grid[row][col] = i
        #         if back_tracking(grid, row, col + 1):
        #             return True

        #         grid[row][col] = 0

        # Add the solution in the GUI
        for i in range(1, 10):
            if valid(grid, row, col, i):
                grid[row][col] = i

                entries[row][col].delete(0, tk.END)
                entries[row][col].insert(0, str(i))

                # Highlight changes
                entries[row][col].config(fg='blue') 
                # Refresh GUI
                parent.update_idletasks()  

                if back_tracking(grid, row, col + 1):
                    return True

                grid[row][col] = 0
                entries[row][col].delete(0, tk.END)
                # Refresh GUI
                parent.update_idletasks()
        
        return False

# Solve and display result 

# if back_tracking(grid, 0, 0):
#     for row in grid:
#         print(row)
# else:
#     print("There's no solution!")

def solve():
    global grid
    if back_tracking(grid):
        messagebox.showinfo("Success", "Sudoku Solved!")
    else:
        messagebox.showerror("Failure", "There is no solution!")

# Add a "Solve" button
solve_button = tk.Button(parent, text="Solve", command = solve, font = ('Arial', 14))
solve_button.grid(row = 9, column=0, columnspan = 9)

# Run the Tkinter main loop
parent.mainloop()
grid = [[9, 2, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 3, 0, 7, 8, 4, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 9, 0, 0],
        [0, 0, 6, 4, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 9, 6, 0, 2, 0],
        [7, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 8, 0, 3, 9, 7, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0]]

# Create a 9x9 grid of entry widgets
entries = [[None for i in range(9)] for i in range(9)]

for row in range(9):
    for col in range(9):
        # Create an input box for each cell in the Sudoku grid.
        entry = tk.Entry(parent, width = 2, font = ('Arial', 30), justify = 'center')
        entry.grid(row = row, column = col, padx = 5, pady = 5)

        # Pre-filled cells
        if grid[row][col] != 0:
            entry.insert(0, str(grid[row][col]))

            # Make the input box read-only
            entry.config(state = 'disabled')

        entries[row][col] = entry


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

    # Check the column whether there is value 'k' in it.
    for i in range(0, 9):
        if grid[row][i] == k:
            not_in_col = False

    # Check the box (sub grid) whether there is value 'k' in it. 
    for i in range(row//3 * 3, row//3 * 3 + 3):
        for j in range(col // 3 * 3, col//3 * 3 + 3):
            if grid[i][j] == k:
                not_in_sub_grid = False
    
    return not_in_row and not_in_col and not_in_sub_grid


# Backtrack every possible cases for suitable number in the grid
def back_tracking(grid, row = 0, col = 0):
    # Base case
    # If check all the board, return True
    # Which is there is solution for the board
    if row == 9:
        return True
    
    # If the column exceed 9, start checking the next row
    elif col == 9:
        return back_tracking(grid, row + 1, 0)
    
    # If that position is already filled with number,
    # move to the next column 
    elif  grid[row][col] != 0:
        return back_tracking(grid, row, col + 1)

    # When that position is blank,
    # Plug the number in (start from 1)
    # If it's met the condition, check the next position
    # until if it's not met, backtrack to the latest position 
    # and change increase the number by 1 until it suitable the case 

    else:
        # for i in range(1, 10):
        #     if valid(grid, row, col, i):
        #         grid[row][col] = i
        #         if back_tracking(grid, row, col + 1):
        #             return True

        #         grid[row][col] = 0


        for i in range(1, 10):
            if valid(grid, row, col, i):
                grid[row][col] = i

                # entries[row][col].delete(0, tk.END)
                entries[row][col].insert(0, str(i))

                # Highlight changes
                entries[row][col].config(fg='blue') 
                # Refresh GUI
                parent.update_idletasks()  

                if back_tracking(grid, row, col + 1):
                    return True

                grid[row][col] = 0
                entries[row][col].delete(0, tk.END)
                # Refresh GUI
                parent.update_idletasks()
        
        return False

# Solve and display result 

# if back_tracking(grid, 0, 0):
#     for row in grid:
#         print(row)
# else:
#     print("There's no solution!")

def solve():
    global grid
    if back_tracking(grid):
        messagebox.showinfo("Success", "Sudoku Solved!")
    else:
        messagebox.showerror("Failure", "There is no solution!")

# Add a "Solve" button
solve_button = tk.Button(parent, text="Solve", command = solve, font = ('Arial', 14))
solve_button.grid(row = 9, column=0, columnspan = 9)

# Run the Tkinter main loop
parent.mainloop()
