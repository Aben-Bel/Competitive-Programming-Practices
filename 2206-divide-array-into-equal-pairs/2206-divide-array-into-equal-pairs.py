class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        
        for i in range(0,len(nums)-1,2):
            if nums[i] != nums[i+1]:
                return False
        return True