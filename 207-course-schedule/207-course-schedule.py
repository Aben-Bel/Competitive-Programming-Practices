class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def topSort(indegree, conn):
            
            queue = deque()
            for node in range(len(indegree)):
                if indegree[node]==0:
                    queue.append(node)
            
            topOrder = []
            while queue:
                cur = queue.popleft()
                topOrder.append(cur)
                for nei in conn[cur]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
                        
            return len(topOrder) == len(indegree)
        
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b]+=1
        
        return topSort(indegree, graph)
        
                    