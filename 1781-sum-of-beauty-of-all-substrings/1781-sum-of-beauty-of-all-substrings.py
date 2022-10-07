class Solution:
    def beautySum(self, s: str) -> int:
        s = list(s)
        ans = 0
        for i in range(len(s)):
            for j in range(i+2,len(s)+1):
                c = Counter(s[i:j])
                ma = max(c.values())
                mi = min(c.values())
                if ma - mi > 0:
                    ans += (ma-mi)
        return ans