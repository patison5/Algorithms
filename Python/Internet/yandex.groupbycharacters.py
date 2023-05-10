# Sample Input ["eat", "tea", "tan", "ate", "nat", "bat"]
# Sample Output [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]

def group_words(words: list[int]) -> list[list[int]]:
	result = []
	result_dict = {}

	for word in words:
		key = "".join(sorted(word))
		if key in result_dict:
			result_dict[key].append(word)
		else:	
			result_dict[key] = [word]

	return [words for words in result_dict.values()]

print(group_words(["eat", "tea", "tan", "ate", "nat", "bat"]))


