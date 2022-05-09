class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = "" 
        for i in range(len(strs[0])):
            temp = strs[0][i]
            for j in range(1, len(strs)):
                if i>=len(strs[j]) or temp != strs[j][i]:
                    return result
            result += temp
        return result
                