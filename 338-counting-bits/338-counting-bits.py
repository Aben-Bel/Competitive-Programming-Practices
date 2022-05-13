class Solution:
    def countBits(self, n: int) -> List[int]:
        bitCounts = [0]*(n+1)
        
        powerTwo = 1
        current = 0
        for i in range(1,n+1):
            if i == powerTwo:
                bitCounts[i] = 1
                powerTwo <<= 1
                current = 1
            else:
                bitCounts[i] = bitCounts[current] + 1
                current += 1
        return bitCounts