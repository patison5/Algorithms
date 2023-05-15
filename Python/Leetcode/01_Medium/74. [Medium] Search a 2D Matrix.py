# 74. [Medium] Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        col = 0
        row = len(matrix[0]) - 1

        while row >= 0 and col <= len(matrix) - 1:
            current_element = matrix[col][row]
            if target == current_element:
                return True
            if target < current_element:
                row -= 1
            else:
                col += 1

        return False




from typing import NamedTuple

class Test(NamedTuple):
    input1: list[list]
    input2: int
    result: int

tests = [
    Test([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True),
    Test([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False),
    Test([[1],[3]], 3, True),
    Test([[1],[3]], 0, False),
    Test([[1]], 1, True),
    Test([[]], 1, False),
    Test([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 23, True)
]

solution = Solution()

for test in tests:

    print("------")
    result = solution.searchMatrix(test.input1, test.input2)
    isPassed = result == test.result
    if (isPassed):
        print("Passed")
    else:
        print(test.input1, test.input2)
        print("Not passed. Exprected: ", test.result, " recieved: ", result) 
        print("\n------")