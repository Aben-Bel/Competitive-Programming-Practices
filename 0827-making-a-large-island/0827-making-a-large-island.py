class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        representative = {}
        size = {}
        inbound = lambda x,y: 0<=x<len(grid) and 0<=y<len(grid[0])
        
        
        def dfs(i,j,visited,parent):
            representative[(i,j)] = parent
            
            
            count = 1
            for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                n_i = dx + i
                n_j = dy + j
                
                if inbound(n_i, n_j) and grid[n_i][n_j] == 1 and (n_i,n_j) not in visited:
                    visited.add((n_i,n_j))
                    count += dfs(n_i,n_j,visited,parent)
            return count
        
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    visited.add((i,j))
                    size[(i,j)] = dfs(i,j,visited, (i,j))
                    
        running_max = 0
        for parent in size:
            running_max = max(running_max, size[parent])
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    calculated_parent = set()
                    temp = 1
                    for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                        n_i = i+dx
                        n_j = j+dy
                        if inbound(n_i, n_j) and grid[n_i][n_j] == 1:
                            parent = representative[(n_i, n_j)]
                            if parent not in calculated_parent:
                                temp += size[parent]
                                calculated_parent.add(parent)
                    running_max = max(temp, running_max)
        return running_max