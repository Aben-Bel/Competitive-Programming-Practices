class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left.bit_length() != right.bit_length():
            return 0
        
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count += 1
        return left << count