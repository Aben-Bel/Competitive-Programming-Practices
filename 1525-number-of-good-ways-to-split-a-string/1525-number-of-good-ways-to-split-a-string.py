class Solution:
    def numSplits(self, s: str) -> int:
        left = []
        right = []
        leftSet = set()
        rightSet = set()
        
        for i in range(len(s)):
            leftSet.add(s[i])
            rightSet.add(s[len(s)-1-i])
            left.append(len(leftSet))
            right.append(len(rightSet))
            
        left = left[::-1]
        count = 0
        for i in range(len(left)-1):                
            if right[i] == left[i+1]:
                count+=1
        
        return count