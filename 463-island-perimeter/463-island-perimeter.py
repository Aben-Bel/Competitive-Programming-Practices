class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
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
            
            
        totalPerimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    totalPerimeter += perimeter(i, j, grid)
        return totalPerimeter