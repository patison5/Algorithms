from typing import NamedTuple

class Test(NamedTuple):
    input: list[int]
    target: int
    result: int

tests: list[Test] = [
    Test([1,3,5,6], 5, 2),
    Test([1,3,5,6], 2, 1),
    Test([1,3,5,6], 7, 4)
]



def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    left = 0
    right = len(nums) - 1

    if target > nums[right]:
        return right + 1

    while left <= right:
        center = (left + right) // 2
        current_value = nums[center]
        if current_value == target:
            return nums.index(current_value)
        if target < nums[center]:
            right = center - 1
        else:
            left = center + 1
    return left


for test in tests:
    searchInsert(test.input, test.target)


for test in tests:
    result = searchInsert(test.input, test.target)
    isPassed = result == test.result
    if (isPassed):
        print("Passed")
    else:
        print("\n------")
        print("Not passed. Exprected: ", test.answer, " recieved: ", result) 
        print("\n------")