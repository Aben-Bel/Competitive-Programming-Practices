class Solution:
    def __init__(self):
        self.mem = {}
        
    def fib(self, n: int) -> int:
        if n==1 or n==0:
            return n
        
        if n in self.mem:
            return self.mem[n]
        
        self.mem[n] = self.fib(n-1) + self.fib(n-2)
        return self.mem[n]