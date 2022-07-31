class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = set()
        seen = {}
        self.longest = -1
        def dfs(node, dis):
            if node == -1:
                return 

            if node not in visited:
                if node in seen:
                    self.longest = max(self.longest, dis - seen[node]+1)
                    return
                seen[node] = dis+1
                dfs(edges[node], dis+1)
                seen.pop(node)
                visited.add(node)
                
                
           
        
        for i in range(len(edges)):
            dfs(i, 1)
        return self.longest
        
            
        