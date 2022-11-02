class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missed = len(nums)
        total = 0
        for i in range(len(nums)):
            missed ^= nums[i]
            total ^= i
        
        return missed ^ total