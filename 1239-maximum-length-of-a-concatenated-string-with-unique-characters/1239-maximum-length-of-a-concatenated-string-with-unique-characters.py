class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def extractBit(val):
            bit = 0
            for char in val:
                temp = ord(char) - ord('a')
                bit |= (1<<temp)
            
            return bit
        
        
                
                
        count = 0
        visited = set()
        def backtrack(i, table):
            nonlocal count
            if i>=len(arr):
                if table not in visited:
                    count = max(count, table.bit_count())
                    visited.add(table)
                return
            if len(set(arr[i])) != len(arr[i]):
                backtrack(i+1,table)
                return
            
            backtrack(i+1, table)
            mask = extractBit(arr[i])
            if mask & table == 0:
                backtrack(i+1, table | mask)
        
        backtrack(0,0)
        return count