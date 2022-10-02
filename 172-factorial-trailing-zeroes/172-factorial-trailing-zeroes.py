class Solution:
    def trailingZeroes(self, n: int) -> int:
        count2 = 0
        count5 = 0
        count10 = 0
        for i in range(2, n+1):
            # if i%10 == 0:
            #     while i%10 == 0:
            #         count10+=1
            #         i/=10
            #     # count10 += len(str(i)[1:])
            # else:
            if i%2==0:
                while i % 2==0:
                    count2 += 1
                    i/=2
            if i%5==0:
                while i % 5==0:
                    count5 += 1
                    i/=5
                
                
        return min(count2, count5)