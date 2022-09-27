class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(i, cummulative):
            if i == len(nums):
                return 1 if cummulative == target else 0
                
            count = dfs(i+1, cummulative + nums[i]) + dfs(i+1, cummulative - nums[i])
            return count 
    
        return dfs(0, 0)