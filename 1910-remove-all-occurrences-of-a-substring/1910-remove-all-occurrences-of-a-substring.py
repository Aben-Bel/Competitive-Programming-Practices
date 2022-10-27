class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # "daabcbaabcbc", part = "abc"
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            
            j=len(part)-1
            k=len(stack)-1
            while j>=0 and k>=0 and stack[k] == part[j]:
                j-=1
                k-=1
            if j == -1:
                count = len(part)
                while stack and count:
                    stack.pop()
                    count -= 1
        
        return "".join(stack)
                
        