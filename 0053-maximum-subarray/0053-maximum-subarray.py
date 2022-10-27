class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runningMax = float('-inf')
        runningSum = 0
        for i in range(len(nums)):
            runningSum = max(nums[i], runningSum + nums[i])
            runningMax = max(runningMax, runningSum)
        
        return runningMax