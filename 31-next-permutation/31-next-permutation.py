class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = len(nums) - 2
        while k>=0 and nums[k] >= nums[k+1]:
            k -= 1
        
        if k==-1:
            nums[:] = reversed(nums[:])
            return
        
        for i in range(len(nums)-1, k-1, -1):
            if nums[i] > nums[k]:
                nums[i], nums[k] = nums[k], nums[i]
                break
        
        nums[k+1:] = reversed(nums[k+1:])
        