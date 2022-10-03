class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        delay = [float('inf')]*n
        
        delay[k-1] = 0
        for i in range(n-1):
            for a,b,w in times:
                if delay[a-1] != float('inf') and delay[a-1]+w < delay[b-1]:
                    delay[b-1] = delay[a-1] + w
        # print(delay)
        res = max(delay)
        return res if res != float('inf') else -1
        
        
            