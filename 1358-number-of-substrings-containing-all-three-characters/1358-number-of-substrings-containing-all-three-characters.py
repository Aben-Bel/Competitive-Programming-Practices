class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        val = {'a':0,'b':0,'c':0}
        
        left = 0
        right = 0
        count = 0
        while left<= right and right < len(s):
            while right < len(s) and (val['a'] <= 0 or val['b'] <= 0 or val['c'] <= 0):
                val[s[right]] += 1
                right += 1

            while left <= right and (val['a'] > 0 and val['b'] > 0 and val['c'] > 0):
                count += (len(s)-right+1)
                val[s[left]] -= 1
                left += 1
                
        
        return count 
                
            
            
                