
from typing import NamedTuple

class Test(NamedTuple):
    nums: list[int]
    k: int
    result: list[int]

tests: list[Test] = [
    Test([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
    Test([-1,-100,3,99], 2, [3,99,-1,-100])
]


def rotate(nums, k):
        """
        :type nums: list[int]
        :rtype: list[int]
        """
        while k > 0:
            last_index = len(nums) - 1
            last_element = nums[last_index]
            nums.pop()
            nums.insert(0, last_element)
            k -= 1

def rotate(nums, k):
        """
        :type nums: list[int]
        :rtype: list[int]
        """
        result_list = []
        for index, number in enumerate(nums):
            current_index = (index + k) % len(nums)
            result_list.insert(current_index, number)
        nums[:] = result_list
        return nums

def rotate(nums, k):
        """
        :type nums: list[int]
        :rtype: list[int]

        # Сдвиг по частям.
        # 1. Полностью разворачиваем набор
        # 2. От начала до K разворачиваем.
        # 3. От K до конца разворачиваем
        """
        if len(nums) <= 1:
            return
        
        k = k % len(nums) 

        nums.reverse()
        left_index = 0
        right_index = k - 1
        while left_index < right_index:
            temp_value = nums[left_index]
            nums[left_index] = nums[right_index]
            nums[right_index] = temp_value
            left_index += 1
            right_index -= 1

        left_index = k
        right_index = len(nums) - 1
        while left_index < right_index:
            temp_value = nums[left_index]
            nums[left_index] = nums[right_index]
            nums[right_index] = temp_value
            left_index += 1
            right_index -= 1
        
        return nums
        
        

for test in tests:
    result = rotate(test.nums, test.k)
    isPassed = result == test.result
    if (isPassed):
        print("Passed")
    else:
        print("\n------")
        print("Not passed. Exprected: ", test.result, " recieved: ", result) 
        print("\n------")