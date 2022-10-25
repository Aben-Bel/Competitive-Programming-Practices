class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        lookUp = {0:1}
        count = 0
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if (prefix - k) in lookUp:
                count += lookUp[prefix-k]
            
            lookUp[prefix] = lookUp.get(prefix, 0) + 1
        
        return count