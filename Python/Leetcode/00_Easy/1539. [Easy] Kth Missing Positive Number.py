# 1539. [Easy] Kth Missing Positive Number

def findKthPositive(arr: list[int], k: int) -> int:
	# last_element_index = len(arr) - 1
	# last_element = arr[last_element_index]
	# missed_inside = last_element - len(arr)
	# missed_outside = k - missed_inside
	# result = 0

	# print("missed_inside:", missed_inside)
	# print("missed_outside:", missed_outside)

	# if (missed_outside > 0):
	# 	result = last_element
	# 	while missed_outside > 0:
	# 		result += 1
	# 		missed_outside -= 1
	# 	return result

	left = 0
	right = len(arr)
	missed_counter = 0

	while left < right:
		center = (left + right) // 2
		missed = arr[center] - center - 1
		if k <= missed:
			right = center
		else:
			left = center + 1

	return k + left



print(findKthPositive([1,2,3,5], 1))
# print(findKthPositive([2,3,4,7,11], 5))
# print(findKthPositive([1,2,3,4,5], 3))
# print(findKthPositive([1,2,5,6,7,8], 9))