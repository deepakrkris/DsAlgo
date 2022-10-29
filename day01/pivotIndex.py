from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftRSum = []
        rightRSum = []
        
        if len(nums) > 0:
            leftRSum.append(0)
            rightRSum.append(0)
        
        for index in range(1, len(nums)):
            leftRSum.append(nums[index - 1] + leftRSum[index - 1])
            rightRSum.append(nums[len(nums) - index] + rightRSum[index - 1])
            

        index = 0
        
        while index < len(nums):
            if leftRSum[index] == rightRSum[len(nums) - index - 1]:
                return index
            index = index + 1
            
        return -1

S = Solution()

print(S.pivotIndex([1, 7, 3, 6, 5, 6]))
print(S.pivotIndex([3, 1, 2]))
print(S.pivotIndex([3, 1, -1]))
print(S.pivotIndex([4, 2, -2, -1, 1, -2, 4]))
print(S.pivotIndex([4, 2, -2, -1, 1, -4, 2]))
