class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # [4,3,2,7,8,2,3,1]
        def cyclicSort():            
            i = 0
            while i<len(nums):
                goTo = nums[i] - 1
                if nums[goTo] != nums[i]:
                    nums[goTo], nums[i] = nums[i], nums[goTo]
                else:
                    i+=1
            
            
        cyclicSort()
        
        ans = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(nums[i])
        return ans
        
                    