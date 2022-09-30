class NumMatrix:
    """
        first build prefix sum by using the immediate top, immediate left and immediate top-left diagonal cells
        when asked for query take the whole square, 
          1. subtract the rectangle ending with top-right starting 0,0
          2. subtract the rectangle ending with left-bottom starting 0,0
         
        that is your calculated sum
    """

    def __init__(self, matrix: List[List[int]]):
        inbound = lambda x, y: 0<=x<len(matrix) and 0<=y<len(matrix[0])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                s= 0
                if inbound(i-1,j-1):
                    s-= matrix[i-1][j-1]
                if inbound(i-1,j):
                    s+= matrix[i-1][j]
                if inbound(i,j-1):
                    s+= matrix[i][j-1]
                matrix[i][j] += s
        
        self.matrix = matrix
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix = self.matrix
        everything = matrix[row2][col2]
        if col1 != 0:
            everything -= matrix[row2][col1-1]
        if row1 != 0:
            everything -= matrix[row1-1][col2]
        if col1 != 0 and row1 != 0:
            everything += matrix[row1-1][col1-1]
        return everything
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)