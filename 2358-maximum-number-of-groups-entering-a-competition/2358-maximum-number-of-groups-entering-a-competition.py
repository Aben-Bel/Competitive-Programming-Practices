class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = 1
        s = 0
        prev = 0
        count = 0
        while s+n<=len(grades):
            count+=1
            s = s+n
            n += 1
        return count
           