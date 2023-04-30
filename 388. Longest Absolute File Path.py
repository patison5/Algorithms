# 388. Longest Absolute File Path

def lengthLongestPath(input):
	"""
	:type input: str
	:rtype: int
	"""
	lines = input.split('\n')
	folders_length_map = {0: 0}
	max_length = 0
	for line in lines:
		name = line.lstrip('\t')
		depth = len(line) - len(name)
		
		if "." in name:
			current_path_length = folders_length_map[depth] + len(name)
			if max_length < current_path_length:
				max_length = current_path_length
		else:
			folders_length_map[depth + 1] = folders_length_map[depth] + len(name) + 1

	return max_length






tests = [
	{
		'line': "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext",
		'answer': 20
	},
	{
		'line': "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",
		'answer': 32
	},
	{
		'line': "a",
		'answer': 0
	},
	{
		'line': "file1.txt\nfile2.txt\nlongfile.txt",
		"answer": 0
	}
]
print("\n\nTESTING\n")
for test in tests:
	result = lengthLongestPath(test['line'])
	isPassed = result == test['answer']
	if (isPassed):
		print("Passed")
	else:
		print("\n------")
		print("Not passed. Exprected: ", test['answer'], " recieved: ", result)	
		print("\n------")