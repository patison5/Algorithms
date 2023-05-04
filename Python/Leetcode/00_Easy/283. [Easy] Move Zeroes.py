# 283. [Easy] Move Zeroes

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    first_zero_index = 0
    for i in range(0, n):
        if nums[i] != 0:
            temp = nums[first_zero_index]
            nums[first_zero_index] = nums[i]
            nums[i] = temp
            first_zero_index += 1
    return nums


nums = [0,1,0,3,12]
print(moveZeroes(nums))
print(nums)