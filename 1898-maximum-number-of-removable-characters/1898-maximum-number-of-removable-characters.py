class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        def check(removed, s, p):
            sp = 0
            pp = 0
            while sp<len(s):
                if sp not in removed and s[sp] == p[pp]:
                    pp += 1
                if pp >= len(p):
                    return True
                sp+=1
            return pp >= len(p)
        
        
        left = 0
        right = len(removable)-1
        best = -1
        while left<=right:
            mid = (left + right)//2
            if check(set(removable[:mid+1]), s, p):
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        return best +1