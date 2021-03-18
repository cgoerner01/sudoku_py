# TO DO:
#save solution
#save and display all possible solutions

from grid import Grid
import copy
class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
        self.grid_copy = copy.deepcopy(grid)
        self.solutions = []

    def set_grid(self, grid: Grid):
        self.grid = grid
        self.grid_copy = copy.deepcopy(grid)
        self.solutions.clear()

    def possible(self, y, x, n):
        for i in range(0,9):
            # if n is already in the column
            if self.grid.get_cell(i, x) == n:
                return False
            # if n is already in the row
            if self.grid.get_cell(y, i) == n:
                return False
        # check if n is in the 3x3 grid
        current_square = self.grid.get_square(y, x)
        for i in range(0,3):
            if n in current_square[i]:
                return False
        return True
    
    def has_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.grid.get_cell(i, j) == 0:
                    return True
        return False
    
    def is_correct(self):
        # if any row contains duplicates, return False
        for i in range(9):
            row = self.grid.get_row(i)
            filtered_row = list(filter(lambda a: a != 0, row))
            if (len(filtered_row) != len(set(filtered_row))):
                return False
        # if any column contains duplicates, return False
        for j in range(9):
            col = self.grid.get_column(j)
            filtered_col = list(filter(lambda a: a != 0, col))
            if (len(filtered_col) != len(set(filtered_col))):
                return False
        # if any 3x3 square contains duplicates, return False
        for a in range(9):
            for b in range(9):
                square = self.grid.get_square(a,b)
                # get all cells of square in one list, filter out 0
                square_list = []
                for sublist in square:
                    for cell in sublist:
                        square_list.append(cell)
                filtered_square_list = list(filter(lambda a: a != 0, square_list))
                if len(filtered_square_list) != len(set(filtered_square_list)):
                    return False
                b += 3
            a +=3
        # if all above conditions fail, the sudoku is correct
        return True

    def get_empty_cells(self):
        result = []
        for y in range(9):
            for x in range(9):
                if self.grid.get_cell(y,x) == 0:
                    print("yayee")
                    tuple = (y,x)
                    result.append(tuple)
        print(result)
        return result

    def solve(self):
        for y in range(9):
            for x in range(9):
                if self.grid.get_cell(y,x) == 0:
                    for i in range(1,10):
                        if self.possible(y,x,i):
                            self.grid.set_cell(y,x,i)
                            self.solve()
                            self.grid.set_cell(y,x,0)
                    return
        self.solutions.append(copy.deepcopy(self.grid))

    def solve_brute_force(self):
        for cell in self.get_empty_cells():
            for i in range(1,10):
                self.grid.set_cell(cell[0], cell[1], i)
                if (not self.has_empty_cell()) and self.is_correct():
                    self.solutions.append(self.grid)
                self.solve_brute_force()
                self.grid.set_cell(cell[0], cell[1], 0)
        
        

    def get_grid(self):
        return self.grid
    
    def get_grid_copy(self):
        return self.grid_copy

    def print_solutions(self):
        for i in range(len(self.solutions)):
            self.solutions[i].printGrid()

    def get_solutions(self):
        return self.solutions

example_grid = Grid()
example_grid.set_grid([[0,4,0,0,0,9,0,2,0],
                       [2,0,0,0,0,7,5,0,0],
                       [0,0,0,0,1,6,7,0,0],
                       [0,0,7,0,0,0,2,0,4],
                       [5,0,0,0,0,0,0,0,3],
                       [4,0,1,0,0,0,9,0,0],
                       [0,0,2,6,5,0,0,0,0],
                       [0,0,4,8,0,0,0,0,1],
                       [0,5,0,1,0,0,0,6,2]])

several_solution_grid = Grid()
several_solution_grid.set_grid([[5,3,0,0,7,0,0,0,0],
                                [6,0,0,1,9,5,0,0,0],
                                [0,9,8,0,0,0,0,6,0],
                                [8,0,0,0,6,0,0,0,3],
                                [4,0,0,8,0,3,0,0,1],
                                [7,0,0,0,2,0,0,0,6],
                                [0,6,0,0,0,0,2,8,0],
                                [0,0,0,4,1,9,0,0,5],
                                [0,0,0,0,8,0,0,0,0]])

def main():
    sudoku_solver = SudokuSolver(several_solution_grid)
    # print(sudoku_solver.possible(6,6,3))
    # print(sudoku_solver.is_correct())
    sudoku_solver.solve()
    sudoku_solver.print_solutions()
    print(len(sudoku_solver.get_solutions()))


main()
