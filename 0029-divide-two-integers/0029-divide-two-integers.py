class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -(2**31) and divisor == -1:
            return (2**31)-1
        
        numOfPositive = 2
        if dividend > 0:
            numOfPositive -= 1
            dividend = -dividend
        
        if divisor > 0:
            numOfPositive -= 1
            divisor = -divisor
            
        quotient = 0
        while dividend <= divisor:
            value = divisor
            powerOfTwo = 1
            
            while value + value >= dividend:
                value += value
                powerOfTwo += powerOfTwo
                
            quotient += powerOfTwo
            dividend -= value
            
        if numOfPositive == 1:
            quotient = -quotient
        
        return quotient
            
            