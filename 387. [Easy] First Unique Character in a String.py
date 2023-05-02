# 387. First Unique Character in a String

class Solution(object):
    def firstUniqChar(self, s):
        for char in s:
            if s.rindex(char) == s.index(char):
                return s.index(char)
        return -1


# Another variant with dictionary

class Solution(object):
    def firstUniqChar(self, s):
        dict = {}
        for char in s:
            if char not in dict:
                dict[char] = {
                    'amount': 1,
                    'position': s.index(char)
                }
            else:
                dict[char]['amount'] += 1

        for key, value in dict.items():
            if value['amount'] == 1:
                return value['position']

        return -1