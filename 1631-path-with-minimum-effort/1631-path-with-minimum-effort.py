class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def getNeighs(i,j):
            inbound = lambda x,y: 0<=x<len(heights) and 0<=y<len(heights[0])
            
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            neighs = []
            for dx, dy in directions:
                ni = i + dx
                nj = j + dy
                if inbound(ni,nj):
                    neighs.append([abs(heights[i][j] - heights[ni][nj]),ni,nj])
            return neighs
                
        visited = set()
        ans = float('inf')
        table = [[float('inf') for j in range(len(heights[i]))] for i in range(len(heights))]
        table[0][0] = 0
        minHeap = [(0,0,0)]
        while minHeap:
            weight, i,j = heapq.heappop(minHeap)
            
            if i==len(heights)-1 and j==len(heights[0])-1:
                return weight
        
            visited.add((i,j))
            for w,ni,nj in getNeighs(i,j):
                if (ni,nj) in visited:
                    continue
                if table[ni][nj] > max(w,weight):
                    table[ni][nj] = max(w,weight)
                    heapq.heappush(minHeap, (max(w,weight), ni,nj))

        return ans