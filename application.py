from sudoku import SudokuSolver
import tkinter as tk
from grid import Grid

window = tk.Tk()
window.geometry("500x500")
bg_color = "#f0ebff"
window.configure(bg=bg_color)
window.title("Sudoku Solver")
cells = Grid().get_grid()

height = 9
width = 9
for i in range(height):
    for j in range(width):
        b = tk.Text(window, background="white", width=4, height=2)
        b.insert(1.0, "0")
        cells[i][j] = b
        b.grid(row=i, column=j)
#if i enter something it needs to be saved

def clear_grid(cells):
    for i in range(9):
        for j in range(9):
            cells[i][j].delete(1.0, "end")
            cells[i][j].insert(1.0, "0")

def solve_grid(cells):
    #create a Grid object with all values from the gui grid
    grid = Grid()
    for i in range(9):
        for j in range(9):
            # get each cell, convert string to int
            grid.set_cell(i,j, int(cells[i][j].get("1.0",'end-1c')))
    #create Sudoku Solver object and calculate solution
    solver = SudokuSolver(grid)
    #TODO:if the input is not a valid sudoku, throw error
    solver.solve()
    # display solution in new window
    solver.print_solutions()
    
def set_example(cells):
    example = [[5,3,0,0,7,0,0,0,0],
               [6,0,0,1,9,5,0,0,0],
               [0,9,8,0,0,0,0,6,0],
               [8,0,0,0,6,0,0,0,3],
               [4,0,0,8,0,3,0,0,1],
               [7,0,0,0,2,0,0,0,6],
               [0,6,0,0,0,0,2,8,0],
               [0,0,0,4,1,9,0,0,5],
               [0,0,0,0,8,0,0,0,0]]
    for i in range(9):
        for j in range(9):
            cells[i][j].delete(1.0, "end")
            cells[i][j].insert(1.0, example[i][j])
    


#buttons
solve_button = tk.Button(text="Solve!", command=lambda:solve_grid(cells))
solve_button.grid(row=0,column=11)

clear_button = tk.Button(text="Clear", command=lambda:clear_grid(cells))
clear_button.grid(row=1, column=11)

example_button = tk.Button(text="Set example", command=lambda:set_example(cells))
example_button.grid(row=2, column=11)


window.mainloop()


