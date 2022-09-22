class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        outPut=[nums[0]]
        sums=nums[0]
        for i in range(1,len(nums)):
            sums=sums+nums[i]
            outPut.append(sums)
            
        return outPut