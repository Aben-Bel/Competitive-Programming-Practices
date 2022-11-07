class Solution:
    def largestOddNumber(self, num: str) -> str:
        idx = len(num)-1
        while idx>= 0 and int(num[idx]) % 2 == 0:
            idx -= 1
        
        return num[:idx+1]