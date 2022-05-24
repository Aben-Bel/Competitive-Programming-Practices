class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        start = 0
        end = n
        
        perm = []
        for char in s:
            if char == "I":
                perm.append(start)
                start += 1
            else:
                perm.append(end)
                end -= 1
        while len(perm) <= n:
            if char == "I":
                perm.append(start)
                start += 1
            else:
                perm.append(end)
                end -= 1
        return perm
        
            