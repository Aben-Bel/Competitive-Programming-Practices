class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        
        seive = [False,False] + [True]*(n-2)
        
        
        i = 2
        while i*i < n:
            if seive[i]:
                inc = 2
                while i*inc < len(seive):
                    seive[i*inc] = False
                    inc+=1
            i+=1            
                    
        return sum(seive)