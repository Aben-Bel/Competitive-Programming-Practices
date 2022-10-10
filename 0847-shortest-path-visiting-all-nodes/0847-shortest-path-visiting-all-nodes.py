class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        min_idx = []
        min_val = float('inf')
        for i in range(len(graph)):
            if len(graph[i]) < min_val:
                min_val = len(graph[i])
        for i in range(len(graph)):
            if len(graph[i])==min_val:
                min_idx.append(i)
       
        def add(bit, val):
            turn =  1<<val
            bit = bit | turn
            return bit

        queue = deque([(idx,1<<idx) for idx in min_idx])
        level = 0
        visited = set()
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                i, set_ = cur
                if set_.bit_count() == len(graph):
                    return level
                
                for nei in graph[i]:
                    temp = set_ | (1<<nei)
                    if (nei, temp) not in visited:
                        queue.append((nei,temp))
                        visited.add((nei,temp))
                    
            level += 1
        return -1