class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def cyclicSort():
            i = 0
            while i<len(nums):
                correct = nums[i]-1
                if 0 < nums[i] < len(nums) and nums[correct] != nums[i]:
                    nums[correct], nums[i] = nums[i],nums[correct]
                else:
                    i+=1
        
        cyclicSort()
        for i, val in enumerate(nums):
            if i+1 != val:
                return i+1
        return len(nums)+1