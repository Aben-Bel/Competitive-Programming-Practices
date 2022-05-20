class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxXor = 0
        l = len(bin(max(nums))) - 2
        
        for i in range(l, -1, -1):
            maxXor <<= 1
            
            prefix = set()
            for num in nums:
                prefix.add(num>>i)
            
            curMax = maxXor | 1
            
            for val in prefix:
                if curMax^val in prefix:
                    maxXor |= curMax
                    break
        
        return maxXor