class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        _dict = set(wordDict)
        dp = [False] * (N + 1)
        dp[N] = True
        
        for i in range(N - 1, -1, -1):
            for word in _dict:
                n = len(word)
                if i + n <= N:
                    dp[i] |= s[i: i + n] in _dict and dp[i + n]
            # for x in range(i, N):
            #     dp[i] |= s[i: x + 1] in _dict and dp[x + 1]
        return dp[0]
        
        
        # @cache
        # def dp(i):
        #     if i >= len(s):
        #         return True
        #     tmp = False
        #     for x in range(i, len(s)):
        #         tmp |= s[i: x + 1] in _dict and dp(x + 1)
        #     return tmp
        # return dp(0)