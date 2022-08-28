class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        N = len(quiet)
        graph = defaultdict(list)
        
        for a, b in richer:
            graph[b].append(a)
        
        ans = [None]*N
        def dfs(node):
            if ans[node] == None:
                ans[node] = node
                for nei in graph[node]:
                    temp = dfs(nei)
                    if quiet[temp] < quiet[ans[node]]:
                        ans[node] = temp
            return ans[node]
        
        return list(map(dfs, range(N)))
                    
                        
                
                
                
                
                
                
                
                
                
                
                
                
                
                