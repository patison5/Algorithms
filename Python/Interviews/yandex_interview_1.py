# // Дан массив N целых чисел, 2 <= N <= 100_000.
# // Необходимо вернуть минимальное произведение двух элементов массива
# // [9, 4, 2, 5, 3] -> 6

def get_minimum_sum(nums: list) -> int:
	sum = 2**31
	for i in range(len(nums)):
		for j in range(len(nums)):
			if i == j:
				continue
			mult = nums[j] * nums[i]
			if mult < sum:
				sum = mult
	return sum


def get_minimum_sum(nums: list) -> int:
	nums = sorted(nums)

	if not nums:
		return 0

	if len(nums) == 1:
		return nums[0]

	return nums[0] * nums[1]	


print(get_minimum_sum([9, 4, 2, 5, 3]))



# Дан набор отсортированных чисел
# Выведите квадраты чисел в остортированном виде
# [-5, -3, -1, 1, 2, 3, 4, 5]
# [1, 1, 4, 9, 9, 16, 25, 25]

l = [-5, -3, -1, 1,2,3,4,5]
left = 0
right = len(l)
result = []

for index, (left_num, right_num) in enumerate(zip(l, l[1:])):
	if left_num <= 0 and right_num > 0:
		left = index
		right = index + 1

while left >= 0 and right < len(l):
	left_num = abs(l[left])
	right_num = l[right]
	if left_num < right_num:
		result.append(left_num**2)
		left -= 1
	else:
		result.append(right_num**2)
		right += 1

while left >= 0:
	result.append(l[left] ** 2)
	left -= 1

while right < len(l):
	result.append(l[right] ** 2)
	right += 1

print(result)


# Дан набор [6,2,3,7,0,1]
# Найти наибольший элемент из поднабора в k элементов

nums = [6,2,3,7,0,1]
k = 3

