class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top = []
        bottom = []
        t=0
        for i in range(len(grid[0])-1,-1,-1):
            t+= grid[0][i]
            top.append(t)
        top = top[::-1]
        top = top + [0]
        
        t=0
        for j in range(len(grid[1])):
            t += grid[1][j]
            bottom.append(t)
        bottom = bottom + [0]
        
        res = float('inf')
        for i in range(len(grid[0])):
            res = min(res, max(top[i+1],bottom[i-1]))
        
        return res
            
        
        