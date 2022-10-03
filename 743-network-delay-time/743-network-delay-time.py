class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, w in times:
            graph[a].append((b,w))
        
        minHeap = [(0,k)]
        delay = [float('inf')]*(n+1)
        delay[k] = 0
        visited = set()
        while minHeap:
            time, node = heapq.heappop(minHeap)
                
            if node in visited:
                continue
            
            visited.add(node)
            for toNode, cost in graph[node]:
                if delay[toNode] > delay[node] + cost:
                    delay[toNode] = delay[node] + cost
                    heapq.heappush(minHeap, (delay[toNode],toNode))
                
        res = max(delay[1:])
        return res if res != float('inf') else -1 
        
        
        
            