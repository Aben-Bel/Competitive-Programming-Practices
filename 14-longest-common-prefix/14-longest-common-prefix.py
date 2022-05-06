class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        
        
        commonPrefix = self.getCommon(strs[0], strs[1])
        for i in range(2, len(strs)):
            commonPrefix = self.getCommon(strs[i], commonPrefix)
        
        return commonPrefix
            
            
    def getCommon(self, str1, str2):
        commonPrefix = ""
        i = 0
        j = 0
        while i<len(str1) and j<len(str2):
            if str1[i] != str2[j]:
                break
            i+=1
            j+=1
        commonPrefix = str1[:i]
        return commonPrefix