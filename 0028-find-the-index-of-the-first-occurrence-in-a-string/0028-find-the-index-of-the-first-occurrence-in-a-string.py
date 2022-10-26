class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def buildLPS(string):
            lps = [0]*len(string)
            
            j = 0
            for i in range(1, len(string)):
                if string[i] == string[j]:
                    lps[i] = j+1
                    j+=1
                elif string[i] != string[j]:
                    j = lps[i-1]
                    while j!=0 and string[i] != string[j]:
                        j = lps[j-1]
                    if string[i] == string[j]:
                        lps[i] = j+1
                        j+=1
                    else:
                        lps[i] = 0
                        
            return lps
        
        # [0, 0, 1, 2, 0]        
        # "ababcabcababababd"
                            # |
        # "ababd"
                # |
        lps = buildLPS(needle)
        
        j=0
        i=0
        while i<len(haystack):
            if haystack[i] == needle[j]:
                j+=1
                i+=1
            else:
                while j!=0 and haystack[i] != needle[j]:
                    j = lps[j-1]
                if haystack[i] != needle[j]:
                    i+=1
            
            if j == len(needle):
                return i-len(needle)
                
        return -1
                
        