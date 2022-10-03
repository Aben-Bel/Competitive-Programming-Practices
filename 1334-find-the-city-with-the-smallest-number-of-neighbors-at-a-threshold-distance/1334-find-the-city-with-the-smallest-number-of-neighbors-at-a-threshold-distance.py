class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[float('inf') if i!=j else 0 for j in range(n)] for i in range(n)]
        
        for a,b,w in edges:
            matrix[a][b] = w
            matrix[b][a] = w
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                for l in range(n):
                    matrix[j][l] = min(matrix[j][l], matrix[j][i]+matrix[i][l])
        
        node = (-1, float('inf'))
        for i in range(len(matrix)):
            count = 0
            for j in range(len(matrix[i])):
                if i!=j and matrix[i][j] <= distanceThreshold:
                    count += 1
                    
            if node[1] >= count:
                node = i, count
            
        return node[0]