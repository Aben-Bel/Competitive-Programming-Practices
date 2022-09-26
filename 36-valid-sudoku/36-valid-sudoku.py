class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        k = int(sqrt(len(board)))
        
        for i in range(0,len(board),k):
            for j in range(0,len(board[0]), k):
                square = set()
                for l in range(i,i+k):
                    for m in range(j,j+k):
                        if board[l][m] != '.' and board[l][m] in square:
                            return False
                        square.add(board[l][m])
        
        for i in range(len(board)):
            horizontal = set()
            for j in range(len(board[0])):
                if board[i][j] != '.' and board[i][j] in horizontal:
                    return False
                horizontal.add(board[i][j])
        
        for i in range(len(board[0])):
            vertical = set()
            for j in range(len(board)):
                if board[j][i] != '.' and board[j][i] in vertical:
                    return False
                vertical.add(board[j][i])
        return True