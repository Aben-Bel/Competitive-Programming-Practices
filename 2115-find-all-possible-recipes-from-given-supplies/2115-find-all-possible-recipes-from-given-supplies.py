class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(set)
        sizeRecipes = len(recipes)
                
        indegrees = defaultdict(int)
        
        supply = set(supplies)        
        r = set(recipes)

        for i in range(sizeRecipes):            
            for ingredient in ingredients[i]:
                if (ingredient in supply or ingredient in r):
                    graph[ingredient].add(recipes[i])
                indegrees[recipes[i]] += 1
                indegrees[ingredient] += 0
                
        queue = deque()
        for i in indegrees:
            if indegrees[i] == 0:
                queue.append(i)

        output = []
        while queue:
            current = queue.popleft()
            
            for c in graph[current]:
                indegrees[c] -= 1
                if indegrees[c] == 0:
                    queue.append(c)  
                    if c in r:
                        output.append(c)
                    
        
        return output