class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()
        results = [0]*n
        for i in range(n-1,-1,-1):
            j = 1
            for k in range(i,n):
                results[i] += j * satisfaction[k]
                j += 1 
        # print(results)
        ans = max(results)
        if ans < 0: return 0
        return ans
    
    
         