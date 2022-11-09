class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = nums[0]
        for num in nums[1:]:
            s ^= num
        
        a, b = 0, 0
        mask = (s & (s-1)) ^ s
        for num in nums:
            if num & mask > 0:
                a ^= num
            else:
                b ^= num
        
        return [a,b]