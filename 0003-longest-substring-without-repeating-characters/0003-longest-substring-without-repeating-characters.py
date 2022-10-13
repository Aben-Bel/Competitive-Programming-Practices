class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            i will use two pointers
            i will move my right if i am not duplicate
            i will move my left if my right is a duplicate
            i will keep track of maximum window before i move left
        """
        if not s:return 0
        l = 0
        r = 0
        seen = set()
        dis = 1
        while l<=r and r<len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
            else:
                seen.remove(s[l])
                l+=1
            dis = max(dis, r-l)
        return dis