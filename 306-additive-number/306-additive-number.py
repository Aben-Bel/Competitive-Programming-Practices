class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def generatePairs(l,m):
            val = num[l:m]
            
            collect = []
            for i in range(1,len(val)):
                a = val[:i]
                if a[0] == '0' and len(a)>1:
                    continue
                for j in range(1,len(val)):
                    b = val[i:i+j]
                    if b[0] == '0' and len(b)>1:
                        continue
                    c = str(int(a)+int(b))
                    res = num[i+j:i+j+len(c)]
                    if c == res:
                        collect.append((i,j))
            return collect
                
        
        pairs = generatePairs(0,len(num))
        for pair in pairs:
            i, j = pair
            a = num[:i]
            b = num[i:i+j]
            c = str(int(a)+int(b))
            res = num[i+j:i+j+len(c)]
            
            if len(a)+len(b)+len(res) == len(num):
                return True
            
            if self.isAdditiveNumber(num[i:]):
                return True
        return False