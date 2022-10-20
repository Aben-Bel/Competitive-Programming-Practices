class Solution:
    def numDecodings(self, s: str) -> int:
       
        @lru_cache(None)
        def backtrack(i):
            if i >= len(s):
                return 1
            
            if s[i] == '0':
                return 0
            
            count = 0
            if int(s[i]) >= 1:
                count += backtrack(i+1) 
            
            if i+1 < len(s) and 1 <= int(s[i:i+2]) <= 26:
                count += backtrack(i+2)
            
            return count
        
        return backtrack(0)