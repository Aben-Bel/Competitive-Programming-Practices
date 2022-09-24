class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s = list(s)
        goal = list(goal)
        count = 0
        toBeSwapped = []
        duplicates = set()
        for i in range(len(s)):
            if s[i] != goal[i]:
                toBeSwapped.append(i)
                count += 1
            duplicates.add(s[i])
                
        if count == 2:
            i, j = toBeSwapped
            s[i],s[j] = s[j],s[i]
            if s == goal:
                return True
            return False
        
        if count == 0:
            return len(duplicates) != len(s)
        
        return False