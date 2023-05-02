# 66. Plus One

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = 1
        for index, el in enumerate(digits):
            idx = len(digits) - index - 1
            sum = sum + digits[idx]
            print(digits[idx], sum)
            if sum <= 9:
                digits[idx] = sum
                sum = 0
            else:

                digits[idx] = sum % 10
                sum = sum // 10
        if sum != 0:
            digits.insert(0, sum)
            
        return digits