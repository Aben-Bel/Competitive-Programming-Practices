class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = [0]*26
        for c in s:
            freq[ord(c)-ord('a')] += 1
        
        
        res = []
        changed = True
        i=25
        prev=24
        while i>=0:
            if freq[i] <= 0:
                i-=1
                continue
            times = min(repeatLimit, freq[i])
            res.extend([chr(ord('a') + i)]*times)
            freq[i] -= times
            
            if freq[i] != 0:
                foundSmaller = False
                for j in range(prev,-1,-1):
                    if j!=i and freq[j] != 0:
                        res.append(chr(ord('a')+j))
                        freq[j] -= 1
                        prev = j
                        foundSmaller = True
                        break
                if not foundSmaller:
                    return "".join(res)
            
                        

        return "".join(res)
                
                