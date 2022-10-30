from typing import List
from collections import deque

class Solution:
    def maxOfWindow(self, nums: List[int], size) -> int:
        slidingMax = []
        if size < len(nums):
            length = len(nums) - size + 1
        else:
            length = 1
            size = len(nums)

        for index in range(length):
            window = [nums[x] for x in range(index, size + index)]
            slidingMax.append(max(window))

        return slidingMax


S = Solution()

# print(S.optimized([4, 5, 6, 1, 2, 3] , 1))
print(S.maxOfWindow([3, 2, 1, 1, 0], 3))
# , S.optimized([3, 2, 1, 1, 0], 3))
print(S.maxOfWindow([3, 4, 2, 4, 3, 5], 4))
# , S.optimized([3, 4, 2, 4, 3, 5], 4))
print(S.maxOfWindow([3, 4, 2, 4, 3, 5], 8))
# , S.optimized([3, 4, 2, 4, 3, 5], 8))
print(S.maxOfWindow([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , 3))
# , S.optimized([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , 3))
