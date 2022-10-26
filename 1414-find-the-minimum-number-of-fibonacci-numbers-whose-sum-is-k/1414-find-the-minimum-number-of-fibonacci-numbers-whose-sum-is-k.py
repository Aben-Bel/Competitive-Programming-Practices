class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1,1]
        while k >= fib[-1] + fib[-2]:
            fib.append(fib[-1]+fib[-2])


        i= len(fib)-1
        step = 0
        while k > 0:# 1
            if k - fib[i] >= 0:
                k = k-fib[i] # 0
                step+=1 # 1
            else:
                i-=1

        return step