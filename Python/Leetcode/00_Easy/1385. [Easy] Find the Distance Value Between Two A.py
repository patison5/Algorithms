# 1385. [Easy] Find the Distance Value Between Two Arrays

def findTheDistanceValue(arr1, arr2, d):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :type d: int
    :rtype: int
    """
    counter = 0
    for number_x in arr1:
        is_valid = True
        print("\n")
        for number_y in arr2:
            if abs(number_x - number_y) <= d:
                is_valid = False
                break
        if is_valid:
            counter += 1
    return counter