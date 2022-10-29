from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rSum = []

        if len(nums) > 0:
            rSum.append(nums[0])
        
        for index in range(1, len(nums)):
            rSum.append(rSum[len(rSum)-1] + nums[index])
            
        return rSum

S = Solution()

print(S.runningSum([3, 4, 5, 6]))
print(S.runningSum([3, 5, 5, 6]))
print(S.runningSum([3, 4, 4, 2, 1]))
