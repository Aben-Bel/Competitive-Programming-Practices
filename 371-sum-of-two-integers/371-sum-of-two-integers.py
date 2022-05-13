class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 01 + 01 = 10
        # 01 + 00 = 01
        # 00 + 01 = 01
        # 00 + 00 = 00
        if (abs(a) < abs(b)): 
            return self.getSum(b, a)
    
        sign =  1 if a > 0 else -1
        
        if a*b >= 0:
            s = abs(a)^abs(b)
            carry = (abs(a)&abs(b))<<1
            while carry:
                temp = s^carry
                carry = (s&carry)<<1
                s = temp
            return s*sign
        else:
            s = abs(a)
            borrow = abs(b)
            while borrow:
                temp = s^borrow
                borrow = ((~s)&borrow)<<1
                s = temp
            return s*sign
            