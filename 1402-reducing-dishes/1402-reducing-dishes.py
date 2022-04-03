class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()
        maxx = -10000
        for i in range(n-1,-1,-1):
            j = 1
            result = 0
            for k in range(i,n):
                result += j * satisfaction[k]
                j += 1 
            maxx = max(maxx, result)
        # print(results)
        
        if maxx < 0: return 0
        return maxx
    
    
         