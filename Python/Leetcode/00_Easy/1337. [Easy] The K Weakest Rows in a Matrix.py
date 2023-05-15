# 1337. [Easy] The K Weakest Rows in a Matrix

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
		dict = {}
		for index, column in enumerate(mat):
			soldiers = 0
			for row in column:
				soldiers += row
			if soldiers not in dict:
				dict[soldiers] = [index]
			else:
				dict[soldiers].append(index)
		
		result = []
		counter = 0
		keys = sorted(list(dict.keys()))

		for key in keys:
			for value in dict[key]:
				if counter < k:
					result.append(value)
				else:
					return result
				counter += 1
		return result

mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
solution = Solution()
solution.kWeakestRows(mat, 3)