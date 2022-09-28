class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False

        for length in range(1,len(s)//2+1):
            if len(s) % length != 0: continue
            first = 0
            second = length
            while second+length <= len(s) and s[first:first+length] == s[second:second+length]:
                first += length
                second += length
            
            if second >= len(s):
                return True
        return False