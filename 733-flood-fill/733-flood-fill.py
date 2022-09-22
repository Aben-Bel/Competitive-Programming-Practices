class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:        
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        def inbound(i,j):
            return 0<=i<len(image) and 0<=j<len(image[0])
        
        def getNeigs(i,j):
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            res = []
            for dx,dy in directions:
                ni = i + dx
                nj = j + dy
                
                if inbound(ni, nj):
                    res.append((ni,nj))
            
            return res
                  
        # recurssion
        def dfs(node,visited):
            visited.add(node)	
            for neighbour_node in getNeigs(node[0], node[1]):
                i,j = neighbour_node
                if(neighbour_node not in visited) and image[i][j] == oldColor:
                    image[i][j] = newColor
                    dfs(neighbour_node, visited)
                    
        image[sr][sc] = newColor
        dfs((sr,sc), set([(sr,sc)]))
        return image