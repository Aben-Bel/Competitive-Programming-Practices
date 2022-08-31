class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
                        
            return topOrder if len(topOrder) == len(indegree) else []
        
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b]+=1
        
        return list(reversed(topSort(indegree, graph)))