class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # [ [1,1,1],
        #   [1,1,1],
        #   [1,1,1]] 
        # -1
        
        # [ [2,2,2],
        #   [2,2,2],
        #   [2,2,2]]
        # 0
        
        # [ [0,0,0],
        #   [0,0,0],
        #   [0,0,0]]
        # 0
        
        # [ [1,2,2],
        #   [2,1,0],
        #   [2,0,1]]
        # -1
        
        # [ [2,1,1],
        #   [1,1,0],
        #   [0,1,1]]
        # 4
        
        # count the number fresh oranges
        # deduct from count
        # i check whether count == 0
        
        # e+v = 4*n*m + n*m = O(n*m)
        # e = 4 direction
        # v = n*m
        
        # go through the grid and collect rotten orange coordinate in queue
        # while collecting, i will count the number of fresh orange
        # if count == 0: 
        #    return 0
        
        # minutes
        # while queue is not empty
            # size of queue
            
            # while size > 0
                # current coordinate in the queue
                # visit all the neighbors
                    # if the neighbor is fresh, # isRotten or isEmpty 
                        # i change to rotten
                        #i will add it to queue
                        # count -= 1
                # size-=1
            # if size > 0:
                # minutes += 1
        # if count == 0:
            # return minutes
        # else:
            # return -1
            
        numberOfFreshOrange = 0
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    numberOfFreshOrange += 1
        
        if numberOfFreshOrange == 0:
            return 0
            
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        minutes = 0
        while queue:
            size = len(queue)
            previousOranges = numberOfFreshOrange
            while size > 0:
                i,j = queue.popleft()
                for direction in directions:
                    newI = i + direction[0]
                    newJ = j + direction[1]
                    
                    if newI >=0 and newI < len(grid):
                        if newJ >=0 and newJ < len(grid[0]):
                            if grid[newI][newJ] == 1:
                                grid[newI][newJ] = 2
                                queue.append((newI, newJ))
                                numberOfFreshOrange -= 1
                size -= 1
            if previousOranges != numberOfFreshOrange:
                minutes += 1
        
        if numberOfFreshOrange == 0:
            return minutes
        return -1
        
        