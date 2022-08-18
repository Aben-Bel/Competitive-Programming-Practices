class Solution:
    def minDominoRotations(self, top: List[int], bottom: List[int]) -> int:
        count = {}
        N= len(top)
        r = 0
        for i in range(N):
            top_val = top[i]
            bottom_val = bottom[i]
            if top_val == bottom_val:
                r+=1
            if top_val in count: count[top_val][0] += 1
            else: count[top_val] = [1,0]
                
            if bottom_val in count: count[bottom_val][1] += 1
            else: count[bottom_val] = [0,1]
            
        ans = float('inf')
        for key in count:
            s = sum(count[key])
            if s-r >= N:
                ans = min(ans, min(count[key][0], count[key][1])-r)
        if ans == float('inf'):
            return -1
        return ans
            