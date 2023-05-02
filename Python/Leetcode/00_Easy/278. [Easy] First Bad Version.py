# 278. [Easy] First Bad Version

def isBadVersion(version):
    if version >= 2:
        return True
    return False

def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    left = 0
    right = n
    center = 0

    if n == 1:
        return 1

    while left <= right:
        center = (left + right) // 2

        if isBadVersion(center) and not isBadVersion(center - 1):
            return center
                
        if isBadVersion(center):
            right = center - 1
        else:
            left = center + 1            

    return center


print(firstBadVersion(2))