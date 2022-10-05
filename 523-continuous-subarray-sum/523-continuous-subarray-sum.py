class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = 0
        seenRemainder = {0:0}
        
        for i in range(len(nums)):
            s += nums[i]
            if s%k in seenRemainder:
                if seenRemainder[s%k] < i:
                    return True
            if s%k not in seenRemainder:
                seenRemainder[s%k] = i+1
        return False