class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        leftIndex = {}
        for i in range(len(s)):
            if s[i] not in leftIndex:
                leftIndex[s[i]] = i
        
        rightIndex = {}
        for i in range(len(s)-1, -1, -1):
            if s[i] not in rightIndex:
                rightIndex[s[i]] = i
        
        maxDis = -1
        for char in s:
            if char in leftIndex and char in rightIndex:
                maxDis = max(maxDis, rightIndex[char] - leftIndex[char] - 1)
        
        return maxDis