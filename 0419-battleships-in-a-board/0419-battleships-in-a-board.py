class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(i, j, board):
            n, m = len(board), len(board[0])
            #horizotal         
            for right in range(j+1, m):
                if board[i][right] == "X":
                    board[i][right] = "."
                else:
                    break

            #vertical move

            for down in range(i+1, n):
                if board[down][j] == "X":
                    board[down][j] = "."
                else:
                    break

        def countNumberOfBattleships(board):
            n, m = len(board), len(board[0])
            battleshipCount = 0
            for i in range(n):
                for j in range(m):
                    if board[i][j]=="X":
                        dfs(i, j, board)
                        board[i][j] = "."
                        battleshipCount +=1

            return battleshipCount
        
        return countNumberOfBattleships(board)