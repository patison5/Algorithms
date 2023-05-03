# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 8-directionally (horizontal and vertical and diagonal) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the amount of an islands in grid. If there is no island, return 0.

from typing import NamedTuple

# // MARK: - Entities --------------------------------------------------------------------------

class Land():
    pass

class Land(NamedTuple):
    row: int
    col: int

# // MARK: - Type defs --------------------------------------------------------------------------

TBoolGrid = list[list[bool]]
TIntGrid = list[list[int]]
TLandGrid = list[list[Land]]
TLandArray = list[Land]

# // MARK: - Global Properties --------------------------------------------------------------------------

already_visited_grid: TBoolGrid = []
whitelisted_lands: TLandArray = []

# // MARK: - Common Methods --------------------------------------------------------------------------

def beautiful_print(grid: TIntGrid):
    for col in grid:
        print("")
        for row in col:
            print(row, end=" ")

def is_position_land(grid: TIntGrid, col: int, row: int) -> bool:
    return True if grid[col][row] == 1 else False

def create_default_visited_grid(size_x, size_y):
    for i in range(0, size_x):
        already_visited_grid.append([])
        for j in range(0, size_y):
            already_visited_grid[i].append(False)

def is_valid(grid: TIntGrid, col: int, row: int) -> bool:
    row_length = len(grid[0])
    col_length = len(grid) 
    return (row >= 0 and row < row_length) and (col >= 0 and col < col_length)


# // MARK: - BFS --------------------------------------------------------------------------

def bfs(grid: TIntGrid, col: int, row: int):
    landsQueue: TLandArray = [Land(row, col)]
    already_visited_grid[col][row] = True
    # print("\nBFS Travers")
    while len(landsQueue) > 0:
        land = landsQueue[0]
        # print("Positions in land", land.col, land.row)
        for row_index in range(land.row - 1, land.row + 2):
            for col_index in range(land.col - 1, land.col + 2):
                if col_index == col and row_index == row: continue
                if not is_valid(grid, col_index, row_index): continue
                if not is_position_land(grid, col_index, row_index): continue
                if already_visited_grid[col_index][row_index]: continue
                newLand = Land(row_index, col_index)
                already_visited_grid[col_index][row_index] = True
                landsQueue.append(newLand)

        # landsQueue.remove(land) 
        del landsQueue[0]

# // MARK: - Main Method --------------------------------------------------------------------------

def maxAreaOfIsland(grid: TIntGrid) -> int:
    already_visited_grid.clear()
    whitelisted_lands.clear()

    create_default_visited_grid(len(grid), len(grid[0]))
    beautiful_print(grid)
    amount_of_islands = 0

    for column_index in range(0, len(grid)):
        for row_index in range(0, len(grid[column_index])):
            if already_visited_grid[column_index][row_index]:
                continue
            is_land = is_position_land(grid, column_index, row_index)
            if is_land:
                bfs(grid, column_index, row_index)
                amount_of_islands += 1

    return amount_of_islands






# // MARK: - Testes --------------------------------------------------------------------------

class Test(NamedTuple):
    grid: list[list[int]]
    result: int

tests: list[Test] = [
    Test([[0,1,1,0], [0,1,1,0], [0,0,1,0], [1,0,0,0], [1,0,1,1]], 3),
    Test([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]], 5),
    Test([[0,0,0,0,0,0,0,0]], 0)
]

for test in tests:
    result = maxAreaOfIsland(test.grid)
    isPassed = result == test.result
    if (isPassed):
        print("Passed")
    else:
        print("\n\n------ TEST ------")
        print("Not passed. Exprected: ", test.result, " recieved: ", result) 
        print("\n----- //TEST -----\n")
