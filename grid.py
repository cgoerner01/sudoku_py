# TODO:
# set_grid: check for validity of grid, otherwise do nothing

class Grid:
    def __init__(self):
        self.grid = [[0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0]]
    
    def set_grid(self, grid):
        self.grid = grid

    def set_cell(self, y, x, n):
        self.grid[y][x] = n

    def get_grid(self):
        return self.grid
        
    def get_cell(self, y, x):
        return self.grid[y][x]

    def get_row(self, n):
        return self.grid[n]

    def get_column(self, n):
        result = []
        for i in range(9):
            result.append(self.grid[i][n])
        return result
    
    def get_square(self, y, x):
        result = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
        # // is floor division -> rounds down to whole number
        # go to the beginning of the 3x3 grid of (y,x)
        x_start = (x//3)*3
        y_start = (y//3)*3
        for i in range(0,3):
            for j in range(0,3):
                result[i][j] = self.grid[y_start + i][x_start + j]
        return result

    def printGrid(self):
        ci = 0
        for i in range(len(self.grid)):
            cj = 0
            for j in range(len(self.grid[i])):
                print(self.grid[i][j], end='')
                print(" ", end = '')
                cj += 1
                if cj == 3 or cj == 6:
                    print("| ", end='')
            print("")
            ci += 1
            if ci == 3 or ci == 6:
                print("---------------------")

    def grid_as_string(self):
        content = ""
        ci = 0
        for i in range(len(self.grid)):
            cj = 0
            for j in range(len(self.grid[i])):
                content = content + str(self.grid[i][j]) + " "
                cj += 1
                if cj == 3 or cj == 6:
                    content = content + "| "
            content = content + "\n"
            ci += 1
            if ci == 3 or ci == 6:
                content = content + "---------------------\n"
        return content