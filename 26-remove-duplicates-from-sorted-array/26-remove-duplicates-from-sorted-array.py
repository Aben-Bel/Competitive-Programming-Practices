class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writeIndex = 1
        for i in range(1, len(nums)):
            if nums[writeIndex-1] != nums[i]:
                nums[writeIndex] = nums[i]
                writeIndex += 1
        return writeIndex