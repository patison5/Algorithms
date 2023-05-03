# 852. [Medium] Peak Index in a Mountain Array

def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left = 0
        right = len(arr) - 1
        while left < right:
            center = (left + right) // 2
            if arr[center] > arr[center + 1]:
                right = center
            else:
                left = center + 1
        return right