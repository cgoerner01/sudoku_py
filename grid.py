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
        #check validity
        self.grid = grid

    def set_cell(self, y, x, n):
        self.grid[y][x] = n

    def get_grid(self):
        return self.grid
        
    def get_cell(self, y, x,):
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



example_grid = [[0,4,0,0,0,9,0,2,0],
                [2,0,0,0,0,7,5,0,0],
                [0,0,0,0,1,6,7,0,0],
                [0,0,7,0,0,0,2,0,4],
                [5,0,0,0,0,0,0,0,3],
                [4,0,1,0,0,0,9,0,0],
                [0,0,2,6,5,0,0,0,0],
                [0,0,4,8,0,0,0,0,1],
                [0,5,0,1,0,0,0,6,2]]

# def main():
#     grid = Grid()
#     grid.set_grid(example_grid)
#     print(grid.get_column(1))
#     print(grid.get_row(1))
#     print(grid.get_square(6,6))
#     grid.printGrid()

# main()