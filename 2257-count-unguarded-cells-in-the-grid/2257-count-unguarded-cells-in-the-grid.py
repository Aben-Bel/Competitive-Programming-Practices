class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for j in range(n)] for i in range(m)]
        for guard in guards:
            grid[guard[0]][guard[1]] = 1
        for wall in walls:
            grid[wall[0]][wall[1]] = 2
            
        def markSeen(r, c):
            i = 1
            while r+i < m:
                if grid[r+i][c] == 1 or grid[r+i][c] == 2:
                    break
                grid[r+i][c] = 3
                i+=1
            
            i = 1
            while r-i >= 0:
                if grid[r-i][c] == 1 or grid[r-i][c] == 2:
                    break
                grid[r-i][c] = 3
                i+=1
            
            i = 1
            while c+i < n:
                if grid[r][c+i] == 1 or grid[r][c+i] == 2:
                    break
                grid[r][c+i] = 3
                i+=1
            
            i = 1
            while c-i >= 0:
                if grid[r][c-i] == 1 or grid[r][c-i] == 2:
                    break
                grid[r][c-i] = 3
                i+=1
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    markSeen(i, j)
                    
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
        
        
        return count
        