class Solution:
    def knightDialer(self, n: int) -> int:
        graph = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]
        
        @lru_cache(None)
        def dfs(i,j,n):            
            if n == 0:
                return 1
            
            if n<0:
                return 0
            
            count = 0 
            inbound = lambda x,y :  0<=x<len(graph) and 0<=y<len(graph[0]) 
            directions = [[2,1],[1,2],[-1,2],[1,-2],[-2,1],[2,-1],[-2,-1],[-1,-2]]
            for dx, dy in directions:
                nx = i+dx
                ny = j+dy
                if inbound(nx,ny) and graph[nx][ny] != -1:         
                    count += dfs(nx,ny,n-1)
                    
            return count
        
        
        count = 0
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if graph[i][j] != -1:
                    count += dfs(i,j,n-1)
        return count % 1000000007
            
                
                