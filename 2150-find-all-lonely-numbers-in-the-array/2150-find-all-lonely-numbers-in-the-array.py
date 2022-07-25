class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        nums.sort()
        ans = []
        
        for i in range(len(nums)):
            if i==0 and i+1<len(nums):
                if nums[i]+1 != nums[i+1] and nums[i+1]!=nums[i]: 
                    ans.append(nums[i])
                continue
            if i==len(nums)-1 and i-1>=0:
                if nums[i]-1 != nums[i-1] and nums[i-1]!=nums[i]: 
                    ans.append(nums[i])
                continue
            if nums[i]+1 != nums[i+1] and nums[i]-1 != nums[i-1]:
                if nums[i] != nums[i+1] and nums[i-1]!=nums[i]:
                    ans.append(nums[i])
        return ans
         