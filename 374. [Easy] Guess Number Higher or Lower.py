# 374. Guess Number Higher or Lower

def guessNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if guess(mid) == 0:
            return mid
        if guess(mid) == 1:
            left = mid + 1
        else:
            right = mid - 1