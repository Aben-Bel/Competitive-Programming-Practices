class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        s1.sort()
        s2.sort()
        inc = True
        dec = True
        for i in range(len(s1)):
            if s1[i] > s2[i]:
                dec = False
            
            if s1[i] < s2[i]:
                inc = False
        
        return inc or dec