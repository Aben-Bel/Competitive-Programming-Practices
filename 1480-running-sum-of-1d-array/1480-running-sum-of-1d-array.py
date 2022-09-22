class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        for i in range(len(nums)):
            sums = 0
            for j in range(0,i+1):
                sums = sums + nums[j]
            output[i] = sums
            
            
            
        return output