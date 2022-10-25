class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2!=0:
            return False
        
        @lru_cache(None)
        def dp(i, bucket1, bucket2):            
            if i>=len(nums):
                return bucket1 == bucket2
            
            return dp(i+1, bucket1+nums[i],bucket2) or dp(i+1, bucket1, bucket2+nums[i])
        
        return dp(0, 0, 0)