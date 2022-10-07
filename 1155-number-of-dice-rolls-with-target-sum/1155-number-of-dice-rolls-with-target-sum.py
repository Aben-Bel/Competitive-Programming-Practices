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
                ans %= 100000007
            return ans
        
        dp = [[0 for j in range(target+1)] for i in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for j in range(1,target+1):
                for l in range(1,k+1):
                    if j-l>=0:
                        dp[i][j] += dp[i-1][j-l]
                        dp[i][j] %= 1000000007
        # print(dp)
        return dp[-1][-1]
                
            
                