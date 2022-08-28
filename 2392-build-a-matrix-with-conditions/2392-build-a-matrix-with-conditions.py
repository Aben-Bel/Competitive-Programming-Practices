class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def topSort(conditions, k):
            outdegree = defaultdict(list)
            indegree = defaultdict(int)
            for edge in conditions:
                a, b = edge
                outdegree[a].append(b)
                indegree[b] += 1

            queue = deque()
            for i in range(1,k+1):
                if indegree[i] == 0:
                    queue.append(i)

            res = []
            while queue:
                cur = queue.popleft()
                res.append(cur)
                for nei in outdegree[cur]:
                    indegree[nei]-=1
                    if indegree[nei] == 0:
                        queue.append(nei)
            return res
        
        
        
        cols = topSort(colConditions, k)
        rows = topSort(rowConditions, k)
        
        if len(rows) < k or len(cols) < k:
            return []
                        
        
        
        pos = {}
        for i in range(1,k+1):
            pos[i] = (rows.index(i), cols.index(i))
        matrix = [[0]*k for i in range(k)]
        for i in range(1,k+1):
            matrix[pos[i][0]][pos[i][1]] = i
        return matrix

        
            
            