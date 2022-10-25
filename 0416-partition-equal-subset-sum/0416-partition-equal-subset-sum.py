class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2!=0:
            return False
        
        @lru_cache(None)
        def dp(i, current):
            if current == total//2:
                return True
            
            if i>=len(nums):
                return False
            
            return dp(i+1, current + nums[i]) or dp(i+1, current)
        
        return dp(0, 0)