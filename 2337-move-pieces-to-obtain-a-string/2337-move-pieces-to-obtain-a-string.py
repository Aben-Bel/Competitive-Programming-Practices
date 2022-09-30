class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s = 0
        t = 0
        while t<len(target) or s<len(start):
            while t<len(target) and target[t] == "_":
                t+=1
            while s<len(start) and start[s] == "_":
                s+=1
            if t>= len(target) and s>=len(start):
                return True
            if t>= len(target) or s>=len(start):
                return False
            
            if target[t] == start[s]:
                if target[t] == "L" and s<t:
                    return False
                if target[t] == "R" and s>t:
                    return False
            else:
                return False
            t+=1
            s+=1
        
        
        return True