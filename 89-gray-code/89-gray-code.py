class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        visited = set()
        visited.add(0)
        
        self.backtrack(n,0,visited, result)
        return result
    
    def backtrack(self, n, cur, visited, result):
        if len(result) == 2**n:
            return True
        
        for i in range(n):
            nextVal = cur ^ (1<<i)
            
            if nextVal not in visited:
                visited.add(nextVal)
                result.append(nextVal)
                
                if self.backtrack(n, nextVal, visited, result): 
                    return True
                
                visited.remove(nextVal)
                result.pop()
                
        return False