class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2: return len(nums)
        writeIndex = 2
        count = 0
        for i in range(2, len(nums)):
            if nums[writeIndex-1] == nums[i] and nums[writeIndex-2] == nums[i]:
                count+=1
                continue
            nums[writeIndex] = nums[i]
            writeIndex += 1
            
        return len(nums)-count