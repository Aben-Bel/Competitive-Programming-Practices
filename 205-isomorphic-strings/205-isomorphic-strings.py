class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        
        match = defaultdict(chr)
        matched = defaultdict(chr)
        for i in range(len(s)):
            if s[i] in match and match[s[i]] != t[i]:
                return False
            
            if t[i] in matched and matched[t[i]] != s[i]:
                return False
            
            match[s[i]] = t[i]
            matched[t[i]] = s[i]
            
        
        return True
        