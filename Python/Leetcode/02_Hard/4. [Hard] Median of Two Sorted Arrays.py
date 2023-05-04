# 4. [Hard] Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

from typing import NamedTuple

def findMedianSortedArrays(nums1, nums2):
    result_list = sorted(nums1 + nums2)
    if len(result_list) % 2 != 0:
        center = len(result_list) // 2
        return result_list[center]
    else:
        center = len(result_list) // 2
        sum = result_list[center] + result_list[center - 1]
        return sum / 2


def findMedianSortedArrays(nums1, nums2):
    if (len(nums1) > len(nums2)):
        return findMedianSortedArrays(nums2, nums1)

    size_n1 = len(nums1)
    size_n2 = len(nums2)
    MAX_INT = 2**63 - 1
    MIN_INT = -MAX_INT

    left = 0
    right = size_n1

    while left <= right:
        center = (left + right) // 2
        cut_n1 = center
        cut_n2 = (size_n1 + size_n2 + 1) // 2 - cut_n1

        left_n1 = MIN_INT if cut_n1 == 0 else nums1[cut_n1 - 1]
        left_n2 = MIN_INT if cut_n2 == 0 else nums2[cut_n2 - 1]
        right_n1 = MAX_INT if cut_n1 == size_n1 else nums1[cut_n1]
        right_n2 = MAX_INT if cut_n2 == size_n2 else nums2[cut_n2]

        if (left_n1 <= right_n2) and (left_n2 <= right_n1):
            if (size_n1 + size_n2) % 2 == 0:
                return (max(left_n1, left_n2) + min(right_n1, right_n2)) / 2
            else:
                return max(left_n1, left_n2)

        if left_n1 > right_n2:
            right = center - 1
        else:
            left = center + 1

    return 0


print(findMedianSortedArrays([3,4], [1,2]))