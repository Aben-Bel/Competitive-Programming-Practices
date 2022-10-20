class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        inbound = lambda x,y : 0<=x<len(board) and 0<=y<len(board[0])
        
        cWord = Counter(word)
        bWord = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                bWord[board[i][j]] = bWord.get(board[i][j], 0) + 1
        
        for key in cWord:
            if key not in bWord or cWord[key] > bWord[key]:
                return False
        
            
        
        def backtrack(i,j,l,visited):
            if l>=len(word):
                return True
            
            for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                ni,nj = dx+i,dy+j
                if inbound(ni,nj) and (ni,nj) not in visited:
                    if board[ni][nj] == word[l]:
                        visited.add((ni,nj))
                        if backtrack(ni,nj,l+1,visited):
                            return True
                        visited.remove((ni,nj))
            return False
                        
        
            
        
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    
                    if backtrack(i,j,1,set([(i,j)])):
                        return True
        
        return False
                        
        
#         [["A","B","C","E"],
#          ["S","F","E","S"],
#          ["A","D","E","E"]]
# "ABCESEEEFS"
                                    