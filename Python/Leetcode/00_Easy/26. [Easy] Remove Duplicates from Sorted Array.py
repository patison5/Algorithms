# 26. [Easy] Remove Duplicates from Sorted Array

def removeDuplicates(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	nums[:] = sorted(set(nums))
	return len(nums)

class Solution:
	def removeDuplicates(self, nums: list[int]) -> int:
		counter = 0
		for i in range(1, len(nums)):
			if nums[i] != nums[counter]:
				counter += 1
				nums[counter] = nums[i]
		return counter + 1

# l = [1,1,2,3,3]
# solution = Solution()
# print(solution.removeDuplicates(l))
# print(l)


class Solution:
	def mergeAlternately(self, word1: str, word2: str) -> str:
		p1 = 0
		p2 = 0
		result = ""
		while p1 < len(word1) or p2 < len(word2):
			if p1 < len(word1):
				result += word1[p1:p1+1]
			if p2 < len(word2):
				result += word2[p2:p2+1]
			p1 += 1
			p2 += 1
			print(p1, p2)
		return result


l1= "ab"
l2 = "pqrs"
solution = Solution()
print(solution.mergeAlternately(l1, l2))