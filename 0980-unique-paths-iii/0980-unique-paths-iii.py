class Solution:
    def __init__(self):
        self.grid = None
        self.full = None
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.grid = grid
        startNode = None
        n, m = len(grid), len(grid[0])
        path = 0
        for i in range(n):
            for j in range(m):
                val = self.getIndex(i,j)
                if grid[i][j] != -1:
                    path = (path | (1<<(val)))
                    
                if grid[i][j] == 1:
                    startNode = (i,j)
        self.full = path
        val = self.getIndex(startNode[0], startNode[1])
        return self.backtrack(startNode[0], startNode[1], 1<<val)
    
    def getIndex(self,i,j):
        n = len(self.grid[0])
        return n*i + j

    @lru_cache(None)
    def backtrack(self, i, j, path):
        if self.grid[i][j] == 2:
            if path == self.full:
                return 1
            else:
                return 0
        
        if self.grid[i][j] == -1:
            return 0
        
        count = 0
        for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            ni = i + dx
            nj = j + dy
            if 0<=ni<len(self.grid) and 0<=nj<len(self.grid[0]):
                val = self.getIndex(ni,nj)
                if path & (1<<(val)):
                    continue
                prev = path
                path = (path | (1<<(val)))
                count += self.backtrack(ni,nj,path)
                path = prev
        
        return count
        
        