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

    def maxWindowV1(self, nums: List[int], size) -> int:
        slidingMax = []

        if size < len(nums):
            length = len(nums) - size + 1
        else:
            size = len(nums)

        sortedWindow = deque()
        sortedWindow.append(0)

        for index in range(1, size) :
            if nums[index] > nums[sortedWindow[0]] :
                sortedWindow.clear()
                sortedWindow.append(index)
            else:
                while nums[sortedWindow[-1]] < nums[index] :
                    sortedWindow.pop()
                sortedWindow.append(index)
  
        slidingMax.append(nums[sortedWindow[0]])

        for index in range(size, len(nums)) :

            while len(sortedWindow) > 0 and sortedWindow[0] < (index - size + 1) :
                sortedWindow.popleft()

            if len(sortedWindow) > 0:
                if nums[index] > nums[sortedWindow[0]] :
                    sortedWindow.clear()
                else :
                    while len(sortedWindow) > 0 and (sortedWindow[-1] < (index - size + 1) or nums[sortedWindow[-1]] < nums[index]) :
                        sortedWindow.pop()

            sortedWindow.append(index)
             
            slidingMax.append(nums[sortedWindow[0]])

        return slidingMax

    def maxWindowFinal(self, nums: List[int], size) -> int:
        window = []

        if size > len(nums):
            size = len(nums)

        q = deque()

        for index in range(size) :
            while q and nums[index] > nums[q[-1]] :
                q.pop()
            q.append(index)

        window.append(nums[q[0]])
        
        for index in range(size, len(nums)) :
            while q and nums[index] > nums[q[-1]] :
                q.pop()
        
            if q and q[0] <= (index - size) :
                q.popleft()

            q.append(index)
            window.append(nums[q[0]])
        
        return window

    def callFn(self, nums: List[int], windowSize) -> int:
        return self.maxWindowFinal(nums, windowSize)

S = Solution()

print(S.callFn([4, 5, 6, 1, 2, 3] , 1))
print(S.callFn([3, 2, 1, 1, 0], 3))
print(S.callFn([3, 4, 2, 4, 3, 5], 4))
print(S.callFn([3, 4, 2, 4, 3, 5], 8))
print(S.callFn([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , 3))
