# 567. [Medium] Permutation in String

class Solution:
	def is_anagram(self, word: str, line: str) -> bool:
		if len(word) != len(line):
			return False
		frequensy_dict = {}
		for char in word:
			if char not in frequensy_dict:
				frequensy_dict[char] = 1
			else:
				frequensy_dict[char] += 1
		
		for char in line:
			if char not in frequensy_dict:
				return False
			frequensy_dict[char] -= 1
			if frequensy_dict[char] < 0:
				return False
		return True

	def checkInclusion(self, s1: str, s2: str) -> bool:
		word = s1
		line = s2
		result = 0
		left = 0
		window_line = ""
		window_sum = 0

		for char in word:
			needed_sum

		for index in range(len(line)):
			window_line += line[index:index+1]
			current_char = line[index]
			window_sum += ord(current_char)
			if len(window_line) == len(word):
				if self.is_anagram(word, window_line):
					return True
				window_line = window_line[1:]
		return False