class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        for i in range(n):
            xor ^= (i^nums[i])
        
        return xor ^ n