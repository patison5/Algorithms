# 1855. [Medium] Maximum Distance Between a Pair of Values

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        p1, p2, result = 0, 0, 0

        while p1 < n1 and p2 < n2:
            if nums1[p1] <= nums2[p2]:
                distance = p2 - p1
                result = max(result, distance)
                p2 += 1
            else:
                p1 += 1
        return result