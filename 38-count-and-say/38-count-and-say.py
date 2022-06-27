class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1: return "1"
        
        s = "1"
        n-=1
        while n>0:
            left = 0 
            right = 0
            say = ""
            while left <= right and right < len(s):
                while right<len(s) and s[left] == s[right]:
                    right+=1
                say += str(right-left) + str(s[left])
                left = right
            s = say
            n-=1
        return s
        