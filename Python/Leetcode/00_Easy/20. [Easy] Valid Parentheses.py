# 20. Valid Parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = []
        if (len(s) == 1): 
            return False

        for char in s:
            if (char == '(') or (char == '{') or (char == "["):
                brackets.append(char)
                continue
            
            if len(brackets) == 0:
                 return False

            if (char == ')') and (brackets[-1] == "("):
                brackets.pop()
                continue
            if (char == '}') and (brackets[-1] == "{"):
                brackets.pop()
                continue
            if (char == ']') and (brackets[-1] == "["):
                brackets.pop()
                continue
            return False
        return len(brackets) == 0


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = []
        leftSide = "([{"
        rightSide = ")]}"

        if len(s) == 1:
            return False

        for char in s:
            if char in leftSide:
                brackets.append(char)
                continue

            if len(brackets) == 0:
                return False

            index = rightSide.index(char)
            print(char, index, rightSide, leftSide)
            if (char in rightSide) and (brackets[-1] == leftSide[index]):
                brackets.pop()
                continue
            return False
        return len(brackets) == 0