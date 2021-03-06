#TODO:
# -prettify
# -german language support
import os
from tkinter.constants import BOTH, FLAT, GROOVE, RIGHT, X, Y
from sudoku import SudokuSolver
import tkinter as tk
from tkinter import Canvas, Label, Scrollbar, Toplevel
from tkinter.filedialog import asksaveasfile 
from grid import Grid
from datetime import date, datetime
import copy
class App:
    def __init__(self, window):
        self.window = window
        self.window.geometry("500x500")
        bg_color = "#f0ebff"
        self.window.configure(bg=bg_color)
        self.window.title("Sudoku Solver")
        self.cells = Grid().get_grid()
        self.error_label = None
        self.initGUI()

    def initGUI(self):
        #sudoku outline
        canvas = Canvas(self.window, height=500, width=500)
        for i in range(10):
            for j in range(10):
                if (i % 3) == 0:
                    canvas.create_line(10, 10 + i*30, 280, 10 + i*30, fill="black", width=2)
                else:
                    canvas.create_line(10, 10 + i*30, 280, 10 + i*30, fill="black", width=1)
                if (j % 3) == 0:
                    canvas.create_line(10 + 30*j, 10, 10 + 30*j, 280, fill="black", width=2)
                else:
                    canvas.create_line(10 + 30*j, 10, 10 + 30*j, 280, fill="black", width=1)
        canvas.pack(fill="both", expand=True)
        #interactive sudoku cells
        for i in range(9):
            for j in range(9):
                b = tk.Text(self.window, background="white", width=1, height=1, relief=FLAT)
                b.bind("<Tab>", self.focus_next_widget)
                b.insert(1.0, "0")
                self.cells[i][j] = b
                b.place(x= 20 + j*30, y = 17 + i*30)
        #buttons
        solve_button = tk.Button(text="Solve!", command=lambda:self.solve_grid())
        solve_button.place(x=300, y=10)

        clear_button = tk.Button(text="Clear", command=lambda:self.clear_grid())
        clear_button.place(x=300, y=40)

        example_button = tk.Button(text="Set example", command=lambda:self.set_example())
        example_button.place(x=300, y=70)
    
    def focus_next_widget(self, event):
        event.widget.tk_focusNext().focus()
        return("break")

    def clear_grid(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(1.0, "end")
                self.cells[i][j].insert(1.0, "0")

    def solve_grid(self):
        self.error_label = None
        #check for edge cases:
        # -input wrong(not int, not 0 to 9)
        try:
            counter = 0
            for i in range(9):
                for j in range(9):
                    tmp = int(self.cells[i][j].get("1.0",'end-1c'))
                    if tmp > 9:
                        self.error_label = Label(self.window, text="The sudoku input was not valid (not a number from 0 to 9)."). place(x=10, y=400)
                        return
                    if tmp != 0:
                        counter += 1
            if counter < 10:
                warning = Label(self.window, text="There are very few given numbers. Computing all possible solutions is not feasible\non generic computers."). place(x=10, y=400)
                return
        except ValueError:
            self.error_label = Label(self.window, text="The sudoku input was not valid (not a number).").place(x=10, y=400)
            return
        # -not enough filled in
        #create a Grid object with all values from the gui grid
        grid = Grid()
        for i in range(9):
            for j in range(9):
                # get each cell, convert string to int
                grid.set_cell(i,j, int(self.cells[i][j].get("1.0",'end-1c')))
        #create Sudoku Solver object and calculate solution
        solver = SudokuSolver(grid)
        #check if sudoku is valid
        if solver.is_correct() is False:
            self.error_label = Label(self.window, text="The given input is not a valid sudoku.").place(x=10, y=400)
            return
        solver.solve()
        # display solution in new window
        if len(solver.get_solutions()) == 0:
            warning = Label(self.window, text="There are no solutions to the given sudoku.").place(x=10, y=400)
        else:
            self.display_solutions(solver)

    def display_solutions(self, solver : SudokuSolver):
        top = Toplevel(self.window, width=300, height=300)
        top.title("Solution")
        scroll = Scrollbar(top)
        canvas = Canvas(top, height=300*len(solver.get_solutions()), width=500, yscrollcommand= scroll.set, scrollregion=(0,0,500,500))
        counter = 0
        for solution in solver.get_solutions():
            for i in range(10):
                for j in range(10):
                    if (i % 3) == 0:
                        canvas.create_line(10, 10 + 290*counter + i*30, 280, 10 + 290*counter + i*30, fill="black", width=2)
                    else:
                        canvas.create_line(10, 10 + 290*counter + i*30, 280, 10 + 290*counter + i*30, fill="black", width=1)
                    if (j % 3) == 0:
                        canvas.create_line(10 + 30*j, 10 + 290*counter, 10 + 30*j, 280 + 290*counter, fill="black", width=2)
                    else:
                        canvas.create_line(10 + 30*j, 10 + 290*counter, 10 + 30*j, 280 + 290*counter, fill="black", width=1)
            for i in range(9):
                for j in range(9):
                    cell = solution.get_cell(i, j)
                    content = tk.Label(top, background="white", width=1, height=1, relief=FLAT, text=cell)
                    content.place(x= 20 + j*30, y = 17 + i*30 + 290*counter)
            counter += 1
        save_button = tk.Button(master=top, text="Save", command=lambda:self.save_solutions(solver))
        save_button.place(x=300, y=10)
        scroll.pack(side = RIGHT, fill= Y)
        scroll.config(command=canvas.yview)
        canvas.pack(fill="both", expand=True)

    def save_solutions(self, solver):
        f = asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        content = "Sudoku Solutions\n{}\nThe given sudoku:\n{}\nThe sudoku has {} solution(s).\n".format(datetime.now(), solver.get_grid_copy().grid_as_string(), len(solver.get_solutions()))
        counter = 1
        for sol in solver.get_solutions():
            content += "(" + str(counter) + ")\n" + sol.grid_as_string() + "\n"
            counter += 1
        f.write(content)
        f.close()

    
    def set_example(self):
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
                self.cells[i][j].delete(1.0, "end")
                self.cells[i][j].insert(1.0, example[i][j])


window = tk.Tk()
application = App(window)
window.mainloop()