class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        _dict = set(wordDict)
        @cache
        def dp(i):
            if i >= len(s):
                return True
            tmp = False
            for x in range(i, len(s)):
                tmp |= s[i: x + 1] in _dict and dp(x + 1)
            return tmp
        return dp(0)