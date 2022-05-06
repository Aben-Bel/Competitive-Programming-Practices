class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charMapStoT = {}
        charMapTtoS = {}
        
        for i in range(len(t)):
            if s[i] in charMapStoT:
                if charMapStoT[s[i]] != t[i]: 
                    return False
            else:
                if t[i] in charMapTtoS and charMapTtoS[t[i]] != s[i]:
                    return False
                charMapStoT[s[i]] = t[i]
                charMapTtoS[t[i]] = s[i]
        return True