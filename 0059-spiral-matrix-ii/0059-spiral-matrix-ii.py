class Solution:
    
    def inbound(self, x,y,n,innerBox):
        n-= innerBox
        if 0+innerBox<=x<n and 0+innerBox<=y<n:
            return True
        
        return False
        
        
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        lets list out the directions
         [[0,1],[1,0],[0,-1],[-1,0]]
        """
        
        matrix = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(0)
            matrix.append(row)
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        current = 0
        row=0
        col=0
        counter=1
        innerBox = 0
        n = n * n
        while n>0:     
            matrix[row][col] = counter
           
            
            dx = directions[current][0]
            dy = directions[current][1]
            if not self.inbound(row+dx,col+dy,len(matrix), innerBox):
                current += 1
                current %= 4
            
            dx = directions[current][0]
            dy = directions[current][1]
            row = row + dx
            col = col + dy
            
            if row == innerBox and col == innerBox:
                innerBox += 1
                row = innerBox
                col = innerBox
                current = 0
            
            counter +=1
            n-=1 
        
        return matrix