class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        lowestMin = 1
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            lowestMin = min(lowestMin, s)
        
        res = 1 - lowestMin
        return res if res > 0 else 1