class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = [0]
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            prefix.append(s)
            
        remainders = {}
        for i in range(len(prefix)):
            remainder = prefix[i] % k
            if remainder in remainders:
                count += remainders[remainder]
            
            remainders[remainder] = remainders.get(remainder, 0) + 1
        
        return count
                