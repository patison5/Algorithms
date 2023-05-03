# 26. [Easy] Remove Duplicates from Sorted Array

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums[:] = sorted(set(nums))
    return len(nums)