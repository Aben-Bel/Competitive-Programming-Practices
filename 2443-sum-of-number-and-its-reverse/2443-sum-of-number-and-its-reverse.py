class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num <= 10:
            if num%2==0:
                return True
            else:
                return False
        def reverseNum(num):
            reversedNum = 0
            while num>0:
                reversedNum *= 10
                reversedNum += (num%10)
                num //= 10
            return reversedNum
        
        for i in range(num+1):
            rnum = int(str(i)[::-1])
            if rnum + i == num:
                return True
        return False
    
    # 720 + 27 = 747
                            
            
            