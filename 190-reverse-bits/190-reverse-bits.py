class Solution:
    def reverseBits(self, x: int) -> int:
        i = 31
        res = 0
        while i>=0:
            val = ((x>>i)&1)
            if val == 1:
                res = res | 1<<(31-i)
            i -= 1
        return res