class Solution:
    def longestPrefix(self, s: str) -> str:
        lsp = [0]*len(s)
        j=0
        for i in range(1,len(lsp)):
            if s[i] == s[j]:
                lsp[i] = j+1
                j+=1
            else:
                while j!=0 and s[i] != s[j]:
                    j = lsp[j-1]
                
                if s[i] == s[j]:
                    lsp[i] = j+1
                    j+=1
                
        # print(lsp)
        return s[:lsp[-1]]