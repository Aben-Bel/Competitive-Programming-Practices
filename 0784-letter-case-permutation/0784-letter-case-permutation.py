class Solution:
    def __init__(self):
        self.ans = set()
        
    def letterCasePermutation(self, s: str) -> List[str]:
        self.backtrack(0,s,0)
        return self.ans
    
    def constructString(self, s,bitmask):
        ans = []
        for i in range(len(s)):
            if s[i].isdigit():
                ans.append(s[i])
            else:
                if bitmask & (1<<i) == 0:
                    ans.append(s[i])
                else:
                    if s[i].isupper():
                        ans.append(s[i].lower())
                    else:
                        ans.append(s[i].upper())
        
        return "".join(ans)
    
    def backtrack(self, i, s, bitmask):
        if i>=len(s):
            self.ans.add(self.constructString(s,bitmask))
            return
        
        
        self.backtrack(i+1, s, bitmask | (1<<i))
        self.backtrack(i+1, s, bitmask)
        
        
            
        
            