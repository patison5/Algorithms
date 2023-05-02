# 35. [Easy] Search Insert Position

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    left = 0
    right = len(nums) - 1

    print(right)

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


searchInsert([1,2,3,4], 4)