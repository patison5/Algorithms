from typing import NamedTuple

class Test(NamedTuple):
    input: list[int]
    result: list[int]

tests: list[Test] = [
    Test([-4,-1,0,3,10], [0,1,9,16,100]),
    Test([-7,-3,2,3,11], [4,9,9,49,121])
]


def sortedSquares(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        position = len(nums) - 1
        result = []
        while (position >= 0):
            if (abs(nums[left]) > abs(nums[right])):
                result.insert(0, nums[left]**2)
                left += 1
                position -= 1
            else:
                result.insert(0, nums[right]**2)
                right -= 1
                position -= 1
        return result


for test in tests:
    result = sortedSquares(test.input)
    isPassed = result == test.result
    if (isPassed):
        print("Passed")
    else:
        print("\n------")
        print("Not passed. Exprected: ", test.result, " recieved: ", result) 
        print("\n------")