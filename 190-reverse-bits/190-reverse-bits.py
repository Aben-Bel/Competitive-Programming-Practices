class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if (n>>(31-i)) & 1:
                res |= (1<<i)
        return res