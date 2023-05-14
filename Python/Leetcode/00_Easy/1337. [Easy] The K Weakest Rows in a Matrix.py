# 1337. [Easy] The K Weakest Rows in a Matrix

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        dict = {}
        for index, column in enumerate(mat):
            print(index, column)
            soldiers = 0
            for row in column:
                soldiers += row
            if soldiers not in dict:
                dict[soldiers] = [index]
            else:
                dict[soldiers].append(index)
        
        result = []
        counter = 0
        counterIndex = 0
        keyIndex = 0
        keys = list(dict.keys())
        print(dict)
        while counter < k:
            key = keys[keyIndex]
            row = dict[key]
            if len(row) <= 0:
                keyIndex += 1
                counterIndex = 0
            else:
                result.append(row[counterIndex])
                counterIndex += 1
                counter += 1
        return result

mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
solution = Solution()
solution.kWeakestRows(mat, 3)