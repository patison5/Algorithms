# 74. [Medium] Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        col = 0
        row = len(matrix[0]) - 1
        print(col, row, len(matrix), len(matrix[0]))
        while row and col < len(matrix) - 1:
            matrix_element = matrix[col][row]
            print(matrix_element)
            if target == matrix[col][row]:
                return True
            if target < matrix_element:
                row -= 1
            else:
                col += 1

        print(col, row)
        print(matrix[1][0])

        if not col and row:
            while row:
                if matrix[col][row] == target:
                    return True
                row -= 1
        return matrix[col][row] == target


solution = Solution()
# print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))

print(solution.searchMatrix([[1],[3]], 3))