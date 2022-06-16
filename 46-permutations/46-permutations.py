class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def generate(first):
            if first >= len(nums):
                result.append(nums[:]) 
            
            for i in range(first, len(nums)):
                nums[i],nums[first] = nums[first], nums[i]
                generate(first+1)
                nums[i],nums[first] = nums[first], nums[i]
        
        generate(0)
        return result