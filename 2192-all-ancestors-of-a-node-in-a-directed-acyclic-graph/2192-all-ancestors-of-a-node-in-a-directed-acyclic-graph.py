class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        indegrees = [0] * n
        
        for edge in edges:
            graph[edge[0]].add(edge[1])
            indegrees[edge[1]] += 1
            
        queue = deque()
        for i in range(n):
            if indegrees[i] == 0:
                queue.append(i)
           
        output = [set() for i in range(n)]
        while queue:
            current = queue.popleft()
            
            for c in graph[current]:
                indegrees[c] -= 1
                output[c].add(current)
                
                if output[current]:
                    output[c].update(output[current])
                    
                if indegrees[c] == 0:
                    queue.append(c)
                    
        result = []
        
        for val in output:
            result.append(sorted(list(val)))
                    
        return result