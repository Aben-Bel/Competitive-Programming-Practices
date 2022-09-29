class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        queue = deque([0])
        usedEdges = set()
        visited = set()
        parent = defaultdict(int)
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                for a in graph[cur]:
                    if a not in visited:
                        parent[a] = cur
                        queue.append(a)
                        visited.add(a)
        count = 0
        usedEdges = set()
        for node in range(len(hasApple)):
            if hasApple[node]:
                cur = node
                while cur != 0:
                    if (cur, parent[cur]) not in usedEdges:
                        count += 1
                    usedEdges.add((cur, parent[cur]))
                    cur = parent[cur]
        return count*2
                            
                    
        
        