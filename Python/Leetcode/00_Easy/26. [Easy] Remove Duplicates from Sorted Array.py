# 26. [Easy] Remove Duplicates from Sorted Array

def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums[:] = sorted(set(nums))
    return len(nums)