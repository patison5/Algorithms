# 167. [Medium] Two Sum II - Input Array Is Sorted

def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left = 0
    right = len(numbers) - 1
    while left != right:
        left_number = numbers[left]
        right_number = numbers[right]
        if left_number + right_number == target:
            return [left + 1, right + 1]
        if left_number + right_number > target:
            right -= 1
        else:
            left += 1