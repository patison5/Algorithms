# https://leetcode.com/problems/add-two-numbers/

tests = [
	{
		'l1': [0],
		'l2': [0],
		'answer': [0]
	},
	{
		'l1': [9,9,9,9,9,9,9],
		'l2': [9,9,9,9],
		'answer': [8, 9, 9, 9, 0, 0, 0, 1]
	},
	{
		'l1': [1,2,3],
		'l2': [4],
		'answer': [5,2,3]
	},
	{
		'l1': [1,2,3],
		'l2': [9],
		'answer': [0,3,3]
	}
]

def addTwoNumbers(l1, l2):
	lengthMax = max(len(l1), len(l2))
	result = []
	intValue = 0

	for i in range(len(l1), lengthMax):
		l1.append(0)

	for i in range(len(l2), lengthMax):
		l2.append(0)

	for i in range(0, lengthMax):
		sum = intValue + l1[i] + l2[i]
		if (sum <= 9):
			result.append(sum)
			intValue = 0
		else:
			intValue = sum // 10
			modValue = sum % 10
			result.append(modValue)
			if (i == lengthMax - 1):
				result.append(intValue)
	return result


for test in tests:
	result = addTwoNumbers(test['l1'], test['l2'])
	isPassed = result == test['answer']
	if (isPassed):
		print("Passed")
	else:
		print("Not passed. Exprected: ", test['answer'], " recieved: ", result)	
	