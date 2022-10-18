class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        dx, dy = -1, 0
        current = 0
        seen = set()
        row = rStart
        col = cStart
        grid = [[0 for _ in range(cols)] for _ in range(rows)]
        ans = []
        
        while len(ans) < rows * cols:
            # print(row, col)
            if grid[row][col] == 0:
                grid[row][col] = 1
                ans.append([row, col])
            else:
                seen.add((row, col))
            if (row, col) not in seen and (not (0 <= row + dy < rows and 0 <= col - dx < cols) or\
                grid[row + dy][col - dx] == 0):
                dx, dy = dy, -dx
            if len(ans) == rows * cols:
                break
            while not (0 <= row + dx < rows and 0 <= col + dy < cols):
                dx, dy = dy, -dx
                
            
            row += dx
            col += dy
        return ans