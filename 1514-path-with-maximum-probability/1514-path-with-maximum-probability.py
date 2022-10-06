class Solution:
    def maxProbability(self, n: int, edge: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)

        
        for i in range(len(edge)):
            graph[edge[i][0]].append((edge[i][1], succProb[i]))
            graph[edge[i][1]].append((edge[i][0], succProb[i]))
        
        
        minHeap = [(-1,start)]
        visited = set()
        table = [float('-inf')]*n
        while minHeap:
            weight, cur = heapq.heappop(minHeap)
            weight = (-1)*weight
            
            if end == cur:
                return weight
            
            for node, w in graph[cur]:                
                if table[node] < w*weight:
                    heapq.heappush(minHeap, ((-1)*(w*weight), node))
                    table[node] = w*weight
        
        return 0
                
                
        
        
            