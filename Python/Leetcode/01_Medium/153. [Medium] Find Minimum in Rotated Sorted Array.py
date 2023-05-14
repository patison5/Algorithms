# 153. [Medium] Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)

        if nums[left] < nums[right-1]:
            return nums[0]

        while left < right:
            center = (left + right) // 2
            if nums[center] < nums[center - 1]:
                return nums[len(nums) - center + 1]
            
            if nums[left] < nums[center]:
                left = center 
            else:
                right = center

        return nums[0]


from typing import NamedTuple

class Test(NamedTuple):
    input: list[int]
    result: int

tests = [
    Test([3,4,5,1,2], 1),
    Test([4,5,6,7,0,1,2], 0),
    Test([11,13,15,17], 11),
    Test([11], 11),
    Test([11, 12], 12),
    Test([2,1], 1)
]

solution = Solution()
for test in tests:
    print("\n-------")
    result = solution.findMin(test.input)
    isPassed = result == test.result
    if (isPassed):
        print("Passed")
    else:
        print(test.input)
        print("Not passed. Exprected: ", test.result, "recieved", result)
        print("------")