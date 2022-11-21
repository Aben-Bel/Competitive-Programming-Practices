class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nextGen = [[0 for j in range(len(board[i]))] for i in range(len(board))]
        
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                numOfOnes = self.getNeis(i,j,board)
                if board[i][j] == 0 and numOfOnes == 3:
                    nextGen[i][j] = 1
                elif board[i][j] == 1 and numOfOnes < 2:
                    nextGen[i][j] = 0
                elif board[i][j] == 1 and (numOfOnes == 2 or numOfOnes == 3):
                    nextGen[i][j] = 1
                elif board[i][j] == 1 and numOfOnes > 3:
                    nextGen[i][j] = 0
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = nextGen[i][j]
        
                    
    
    def getNeis(self, i,j,board):
        directions = [[1,0],[0,1],[-1,0],[0,-1],[-1,1],[1,-1],[-1,-1],[1,1]]
        inbound = lambda x,y : 0<=x<len(board) and 0<=y<len(board[0])
        count = 0
        for dx, dy in directions:
            n_i = dx + i
            n_j = dy + j
            
            if inbound(n_i, n_j):
                count += board[n_i][n_j]
        
        return count
                