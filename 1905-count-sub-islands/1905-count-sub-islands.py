class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def getNeighs(i,j):
            inbound = lambda x, y: 0<=x<len(grid1) and 0<=y<len(grid1[0])
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            neighs = []
            for dx, dy in directions:
                ni = i + dx 
                nj = j + dy
                if inbound(ni, nj) :
                    neighs.append((ni,nj))
            return neighs
        
        def dfs(node):
            res = True
            x,y = node 
            grid2[x][y] = 0
            for nei in getNeighs(node[0], node[1]):
                i, j = nei
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    res = False
                elif grid2[i][j] == 1 and grid1[i][j] == 1:
                    res &= dfs((i,j))
            return res
        count = 0
        visited = set()
        for i in range(len(grid1)):
            for j in range(len(grid1[i])):
                if grid1[i][j] == 1 and grid2[i][j] == 1:
                    # print('i:',i,'j:',j)
                    if dfs((i,j)):
                        # print((i,j))
                        count += 1
        return count
    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
        
                