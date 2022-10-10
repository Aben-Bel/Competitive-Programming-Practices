class Solution:
    def robotWithString(self, s: str) -> str:
        t = []
        p = []
        c = [0]*26
        for ch in s:
            c[ord(ch)-ord('a')] += 1
        
        k=0
        for ch in s:
            t.append(ch)
            c[ord(ch)-ord('a')] -= 1           
            while k <len(c) and c[k]==0:
                k+=1
            
            while t and (ord(t[-1]) - ord('a')) <= k:
                p.append(t.pop())
        while t:
            p.append(t.pop())
            
        
        return "".join(p)