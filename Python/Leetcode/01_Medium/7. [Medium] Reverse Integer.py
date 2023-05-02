# 7. Reverse Integer

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    isNegative = x < 0
    result = int(str(abs(x))[::-1])

    if result < 2 ** 31 - 1:
        return result * -1 if isNegative else result
    else:
        return 0