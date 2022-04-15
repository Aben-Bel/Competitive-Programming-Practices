class DisjointSet:
    def __init__(self, n, m, grid):
        self.rank = [[grid[i][j] for j in range(m)] for i in range(n)]  
        self.root = [[(i,j) for j in range(m)] for i in range(n)]  
        self.n = n
        self.m = m
        
    def find(self, pi, pj):
        if self.root[pi][pj] == (pi, pj):
            return (pi, pj)
        
        i, j = self.root[pi][pj]
        self.root[pi][pj] = self.find(i, j)        
        return self.root[pi][pj]
    
    
    def union(self, n1i, n1j, n2i, n2j):        
        n1ri, n1rj = self.find(n1i, n1j)
        n2ri, n2rj = self.find(n2i, n2j)
        
        if (n2ri, n2rj) != (n1ri, n1rj): 
            if self.rank[n1ri][n1rj] > self.rank[n2ri][n2rj] :
                self.root[n2ri][n2rj]  = (n1ri,n1rj)
                self.rank[n1ri][n1rj] += self.rank[n2ri][n2rj]

            else:
                self.root[n1ri][n1rj]  = (n2ri,n2rj)
                self.rank[n2ri][n2rj] += self.rank[n1ri][n1rj] 
    
    def getMaxArea(self):
        m = 0
        for i in range(self.n):
            for j in range(self.m):
                m = max(m, self.rank[i][j])
        return m

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        directional = [[0,1],[1,0],[0,-1],[-1,0]]
        
        disjoint = DisjointSet(n,m, grid)
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    for direction in directional:
                        row = direction[0] + r
                        column = direction[1] + c
                        
                        if row < 0 or column >= m or row >= n or column < 0:
                            continue
                        
                        if grid[row][column] == 1:
                            disjoint.union(r,c,row,column)
                            
        return disjoint.getMaxArea()