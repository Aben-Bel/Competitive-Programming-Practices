class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        numOfObstacles = 0
        startNode = None
        n,m = len(grid), len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == -1:
                    numOfObstacles += 1
                if grid[i][j] == 1:
                    startNode = (i,j)
        
        return self.backtrack(startNode[0], startNode[1], grid, set([startNode]), numOfObstacles)
    
    def backtrack(self, i, j, grid, path, numOfObstacles):
        if grid[i][j] == 2:
            if len(path) == (len(grid)*len(grid[0]) - numOfObstacles):
                return 1
            else:
                return 0
        
        if grid[i][j] == -1:
            return 0
        
        count = 0
        for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            ni = i + dx
            nj = j + dy
            if 0<=ni<len(grid) and 0<=nj<len(grid[0]):
                if (ni,nj) in path:
                    continue
                    
                path.add((ni,nj))
                count += self.backtrack(ni,nj,grid,path,numOfObstacles)
                path.remove((ni,nj))
        
        return count
        
        