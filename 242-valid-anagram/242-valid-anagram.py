class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ct = Counter(t)
        cs = Counter(s)
        
        
        for i in range(len(s)):
            if cs[s[i]] != ct[s[i]]:
                return False
        return True