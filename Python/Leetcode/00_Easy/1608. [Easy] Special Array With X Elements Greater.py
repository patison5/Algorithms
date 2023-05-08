# 1608. [Easy] Special Array With X Elements Greater Than or Equal X

def amount_of_elements_that_greater_then(nums: list[int], n: int) -> bool: 
	counter = 0
	for number in nums:
		if number >= n:
			counter += 1
	return counter

def specialArray(nums: List[int]) -> int:
	left = 0
	right = len(nums)
	while left <= right:
		center = (left + right) // 2
		amount = amount_of_elements_that_greater_then(nums, center)
		
		if amount == center:
			return amount
		if amount > center:
			left = center + 1
		else:
			right = center - 1
	
	return -1