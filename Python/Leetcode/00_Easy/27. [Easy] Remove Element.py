# 27. [Easy] Remove Element

class Solution:
	def removeElement(self, nums: list[int], val: int) -> int:
		counter = 0
		while counter < len(nums):
			number = nums[counter]
			if number == val:
				nums.remove(number)
				counter -= 1
			counter += 1
		return len(nums)

solution = Solution()
arr = [2]
print(solution.removeElement(arr, 2))