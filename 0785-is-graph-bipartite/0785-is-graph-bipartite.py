class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        for i in range(len(graph)):
            if i not in colors:
                colors[i] = 0
                stack = [i]
                while stack:
                    cur = stack.pop()
                    for nei in graph[cur]:
                        if nei in colors:
                            if colors[nei]==colors[cur]: return False
                        else:
                            colors[nei] = colors[cur]^1
                            stack.append(nei)
        return True
                    
                
        
