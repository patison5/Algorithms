# 33. [Medium] Search in Rotated Sorted Array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # мы находимся в левой отсортированной части
                if nums[left] <= target and nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # мы находимся в правой отсортированной части
                if nums[right] >= target and nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1