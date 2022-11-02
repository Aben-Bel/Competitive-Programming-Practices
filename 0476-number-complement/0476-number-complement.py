class Solution:
    def findComplement(self, num: int) -> int:
        x = 1
        size = floor(log2(num)) + 1
        x <<= size
        x-=1
        num^=x
        return num