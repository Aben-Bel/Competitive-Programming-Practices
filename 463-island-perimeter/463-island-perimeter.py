class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def getNeis(i,j,grid):
            N=len(grid)
            M= len(grid[0])
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            inbound = lambda i,j : 0<= i <N and 0<= j <M
            result = []
            for xv, yv in directions:
                nx = xv + i 
                ny = yv + j
                if inbound(nx,ny):
                    result.append((nx,ny))
            return result
        
        def perimeter(i,j, grid):
            N=len(grid)
            M= len(grid[0])
            inbound = lambda i,j : 0<= i <N and 0<= j <M
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            result = 0
            for xv, yv in directions:
                nx = xv + i 
                ny = yv + j
                if inbound(nx,ny):
                    if grid[nx][ny] == 0:
                        result += 1
                else:
                    result += 1
            return result
            
            
        self.totalPerimeter = 0
        def dfs(i,j,grid,visited):
            if (i,j) in visited:
                return 0
            if grid[i][j] == 0:
                return 0
            
            visited.add((i,j))
            s = perimeter(i,j,grid)
            for x,y in getNeis(i,j,grid):
                s += dfs(x,y,grid,visited)
            return s
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j,grid,set())
                    
        return 0