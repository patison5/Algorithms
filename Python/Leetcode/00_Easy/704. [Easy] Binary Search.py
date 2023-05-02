# 704. [Easy] Binary Search

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:
        center = (left_index + right_index) // 2
        if target == nums[center]:
            return center
        if target > nums[center]:
            left_index = center + 1
        else:
            right_index = center - 1
    else:
        return -1


print(search([-1,0,3,5,9,12], 12))