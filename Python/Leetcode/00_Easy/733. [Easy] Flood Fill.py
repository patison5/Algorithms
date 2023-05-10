# 733. [Easy] Flood Fill

from typing import NamedTuple

class Pixel(): pass


TPixelGrid = list[list[Pixel]]
TPixelArray = list[Pixel]
TIntGrid = list[list[int]]
TBoolGrid = list[list[bool]]


class Pixel(NamedTuple):
    col: int
    row: int
    color: int


class Solution:
    def is_valid(self, grid: TIntGrid, col: int, row: int):
        col_length = len(grid)
        row_length = len(grid[0])
        return (col >= 0 and col < col_length) and (row >= 0 and row < row_length)

    def is_pixel_whitelisted(
        self,
        grid: TIntGrid,
        column: int, 
        row: int,
        color: int
    ) -> bool:
        return grid[column][row] == color

    def create_default_visited_grid(self, grid: TIntGrid, already_visited_grid: TBoolGrid):
        column_size = len(grid)
        row_size = len(grid[0])
        for i in range(column_size):
            already_visited_grid.append([])
            for _ in range(row_size):
                already_visited_grid[i].append(False)

    def is_visited(self, grid: TBoolGrid, col: int, row: int) -> bool:
        return grid[col][row]

    def set_grid_color(self, grid, pixel: Pixel, color: int):
        grid[pixel.col][pixel.row] = color

    def dfs(
        self,
        grid: TIntGrid,
        visited_grid: TBoolGrid,
        col: int,
        row: int,
        color: int
    ):
        pixel_color = grid[col][row]
        neighbours_queue: TPixelArray = [Pixel(col, row, pixel_color)]
        visited_grid[col][row] = True
        while neighbours_queue:
            pixel = neighbours_queue[0]
            grid[pixel.col][pixel.row] = color
            available_neighbors_positions = [
                (pixel.col - 1, pixel.row),
                (pixel.col + 1, pixel.row),
                (pixel.col, pixel.row - 1),
                (pixel.col, pixel.row + 1)
            ]
            for neighbor_position in available_neighbors_positions:
                neighbor_col = neighbor_position[0]
                neighbor_row = neighbor_position[1]

                if not self.is_valid(grid, neighbor_col, neighbor_row):
                    continue
                if self.is_visited(visited_grid, neighbor_col, neighbor_row):
                    continue
                if not self.is_pixel_whitelisted(grid, neighbor_col, neighbor_row, pixel_color):
                    continue

                visited_grid[neighbor_col][neighbor_row] = True
                neighbor_color = grid[neighbor_col][neighbor_row]
                neighbours_queue.append(Pixel(neighbor_col, neighbor_row, neighbor_color))
            del neighbours_queue[0]


    def beautiful_print(self, grid: TIntGrid):
        for col in grid:
            print("")
            for row in col:
                print(row, end=" ")

    def floodFill(
        self, 
        image: TIntGrid, 
        sc: int, 
        sr: int, 
        color: int
    ) -> TIntGrid:
        already_visited_grid: TBoolGrid = []
        self.create_default_visited_grid(image, already_visited_grid)
        self.dfs(image, already_visited_grid, sc, sr, color)
        self.beautiful_print(image)
        return image



solution = Solution()
solution.floodFill(
    [[1,1,1],[1,1,0],[1,0,1]],
    1,
    1,
    2
)