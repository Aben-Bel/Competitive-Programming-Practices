class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        def cyclicSort():
            i = 0
            while i<len(nums):
                takeTo = nums[i]-1
                if nums[takeTo] != nums[i]:
                    nums[takeTo], nums[i] = nums[i], nums[takeTo]
                else:
                    i+=1
        
        
        cyclicSort()
        ans = []
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                ans.append(i+1)
        return ans