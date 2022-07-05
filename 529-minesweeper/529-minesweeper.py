class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        #helper functions
        def checkBoundary(row, col):
            if row >= len(board):
                return False
            if row < 0:
                return False
            if col >= len(board[0]):
                return False
            if col < 0:
                return False
            return True
        
        def getNeighbors(row, col):
            directions = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,-1],[-1,1]]
            neighbors = []
            for direction in directions:
                newR = row + direction[0]
                newC = col + direction[1]
                
                if checkBoundary(newR, newC):
                    neighbors.append((newR, newC))
                
            return neighbors
        
        def countNumOfMines(neighbors):
            count = 0
            for neighbor in neighbors:
                if board[neighbor[0]][neighbor[1]] == 'M':
                    count+=1
            return count
        
        # Solution
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        stack = [(click[0], click[1])]
        
        while stack:
            curr = stack.pop()
            # check all the neighbors
            neighbors = getNeighbors(curr[0], curr[1])
            
            # count number of mines around its neighbors
            countMines = countNumOfMines(neighbors)
            
            if countMines == 0:
                board[curr[0]][curr[1]] = 'B'
                for neighbor in neighbors:
                    if board[neighbor[0]][neighbor[1]] == 'E':
                        stack.append(neighbor)
            else:
                board[curr[0]][curr[1]] = str(countMines)
                
        return board
                
        
        
        # [["E","E","E","E","E"],
        #  ["E","E","M","E","E"],
        #  ["E","E","E","E","E"],
        #  ["E","E","E","E","E"]]
            # [["B","B","1","B","B"],
            #  ["B","1","M","1","B"],
            #  ["B","B","1","B","B"],
            #  ["B","B","B","B","B"]]
        
        # click = [3,0] 
        
        # test case 1 = [['M']] and click = [0,0]
        # test case 2 = [['E','B'],['B','B']] and click = [0,0]
        # given test cases
        
        # time: O(V+E)-> 8*V + V = 9*V = |V = numberofRows*numberofCol = O(m*n)|
        #                 E    V
        # space: O(m*n)
        
        # psuedo code
        # check whether clicked place is not mine
            # change the cell to X and return board
        # push to stack
            # do dfs if it isnot 'B'
                # if all node's neighbor is Empty, count of mines == 0 
                    # change to B before pushing
                    # push to stack
                # elseif the neighbor have a mine
                    # count the number of mine and set it
        # return the board