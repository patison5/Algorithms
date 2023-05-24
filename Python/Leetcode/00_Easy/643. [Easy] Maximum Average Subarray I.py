# 643. [Easy] Maximum Average Subarray I

from collections import deque

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        result = - 2 ** 31 - 1
        window_sum = 0
        counter = 0
        for index in range(len(nums)):
            counter += 1
            window_sum += nums[index]
            if counter == k:
                result = max(result, window_sum / k)
            if counter > k:
                window_left_index = index - k
                window_sum -= nums[window_left_index]
                result = max(result, window_sum / k)
        return result

solution = Solution()
print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))