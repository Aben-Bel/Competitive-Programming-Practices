class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ts = Counter(t)
        count = len(t)
        ans = float('inf')
        i = 0
        l = 0
        r = 0
        while r < len(s):
            char = s[r]
            if char in ts:
                if ts[char] > 0:
                    count -= 1
                ts[char] -= 1
            r += 1
            
            while count <= 0:
                t = r - l
                if ans > t:
                    ans = t
                    i = l
                char = s[l]
                if char in ts:
                    if ts[char] >= 0:
                        count += 1
                    ts[char] += 1
                l += 1
        if ans != float('inf'):
            return s[i: i+ans]
        return ''