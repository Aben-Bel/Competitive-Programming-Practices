class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        
        def dfs(node,graph,colors):
            for nei in graph[node]:
                if nei in colors:
                    if colors[nei] == colors[node]:
                        return False
                else:
                    colors[nei] = colors[node]^1
                    if not dfs(nei,graph,colors): return False
            return True
        
        for i in range(len(graph)):
            if i not in colors:
                colors[i] = 0
                if not dfs(i,graph,colors):
                    return False
        return True
                    
                
        
