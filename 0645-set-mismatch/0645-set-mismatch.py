class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        missing = None
        duplicate = None
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                duplicate = nums[i]
            elif nums[i] + 1 != nums[i+1]:
                missing = nums[i]+1
            
        if not missing:
            if nums[0] != 1:
                missing = 1
            else:
                missing = len(nums)
    
    
        return [duplicate, missing]
                