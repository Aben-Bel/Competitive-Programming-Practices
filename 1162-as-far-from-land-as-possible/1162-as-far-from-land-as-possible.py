class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        def getNeighs(i,j):
            inbound = lambda x,y : 0<=x<len(grid) and 0<=y<len(grid[0])
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            neighs = []
            for dx, dy in directions:
                ni = i + dx
                nj = j + dy
                if inbound(ni,nj):
                    neighs.append((ni,nj))
            return neighs
        
        visited = set()
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    visited.add((i,j))
        
        level = 1
        mark = [[float('inf') for j in range(len(grid[i]))] for i in range(len(grid))]
        
        while queue:
            size = len(queue)
            for _ in range(size):
                i,j = queue.popleft()
                for nei in getNeighs(i,j):
                    if nei in visited: continue
                    k,l = nei
                    if grid[k][l] == 0 and mark[k][l] > level:
                        mark[k][l] = level
                        visited.add((k,l))
                        queue.append((k,l))
            level+=1
            
        m = float('-inf')
        for i in range(len(mark)):
            for j in range(len(mark[i])):
                if grid[i][j] == 0:
                    m = max(m, mark[i][j])
        return m if m!=float('inf') and m!=float('-inf') else -1
                    
                