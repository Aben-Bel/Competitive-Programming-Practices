class Solution:
    def isHappy(self, n: int) -> bool:
        prev = set([n])
        while n != 1:
            l = str(n)
            s = 0
            for c in l:
                s += int(c)*int(c)
            
            n = s
            if n in prev or n == 1:
                return n == 1
            prev.add(n)
            
        return True