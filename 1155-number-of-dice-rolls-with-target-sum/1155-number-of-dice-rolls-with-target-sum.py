class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @lru_cache(None)
        def recurse(n,target):     
            if n==0 and target == 0:
                return 1

            if n==0 or target < 0:
                return 0
            ans = 0
            for i in range(1,k+1):
                ans += recurse(n-1,target-i)
                ans %= 1000000007
            return ans
        
        return recurse(n,target)
                