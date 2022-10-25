class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        window = 1
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            while (i-left+1 - max(count.values())) > k:
                count[s[left]] = count.get(s[left], 0) - 1
                left+=1
                
            window = max(window, i-left+1)
        return window