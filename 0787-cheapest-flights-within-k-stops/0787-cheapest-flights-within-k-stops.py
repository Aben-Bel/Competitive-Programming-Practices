class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(set)
        for flight in flights:
            a,b,w = flight
            graph[a].add((b,w))
        
        table = [float('inf')]*n
        table[src] = 0
        queue = deque([src])
        level = 0
        while queue:
            copy = table[::]
            for _ in range(len(queue)):
                a = queue.popleft()
                for b,w in graph[a]:
                    if table[a] + w < copy[b]:
                        copy[b] = table[a] + w
                        queue.append(b)
        
            level += 1
            table = copy
            if level == k + 1:
                break
                
        return table[dst] if table[dst] != float('inf') else -1
            
                    
                
                
                