# 34. [Medium] Find First and Last Position of Element in Sorted Array

class Solution:        
    def left_BS(self, nums: list[int], target: int) -> list[int]:
        left_index = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            center = (left + right) // 2

            if nums[center] == target:
                left_index = center
                right = center - 1
            elif nums[center] > target:
                right = center - 1
            else:
                left = center + 1
                
        return left_index
    
    def right_BS(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1
        right_index = -1
        while left <= right:
            center = (left + right) // 2

            if nums[center] == target:
                right_index = center
                left = center + 1
            elif nums[center] < target:
                left = center + 1
            else:
                right = center - 1

        return right_index

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left_index = self.left_BS(nums, target)
        right_index = self.right_BS(nums, target)
        return [left_index, right_index]

solution = Solution()
print(solution.searchRange([5,7,7,8,8,10], 8)) # [3, 4]
print(solution.searchRange([5,7,7,8,8,10], 6)) # [-1, -1]
print(solution.searchRange([], 6)) # [3, 4]]
print(solution.searchRange([2, 2], 3))
print(solution.searchRange([2,2], 2)) # [0,1]


print(len([1,2]))