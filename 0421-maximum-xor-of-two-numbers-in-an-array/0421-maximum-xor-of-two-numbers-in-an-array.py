class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:        
        maxXor = 0
        for i in range(32,-1,-1):
            prefix = set() 
            
            for val in nums:
                prefix.add(val>>i)
                
            maxXor <<= 1
            curMax = maxXor | 1
            
            for val in prefix:
                if val ^ curMax in prefix:
                    maxXor |= curMax
                    break
        
        return maxXor