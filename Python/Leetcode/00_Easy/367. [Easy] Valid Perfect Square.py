# 367. [Easy] Valid Perfect Square

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num
        while left <= right:
            center = (left + right) // 2
            if center * center == num:
                return True
            if center * center > num:
                right = center - 1
            else:
                left = center + 1
        return False