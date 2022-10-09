class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            if i==0 or nums[i-1] != nums[i]:
                left = i+1
                right = len(nums)-1
                while left<right:
                    if nums[left]+nums[right]+nums[i] == 0:
                        res.add((nums[i],nums[left],nums[right]))
                    if nums[left]+nums[right]+nums[i] > 0:
                        right-=1
                    else:
                        left += 1
        return res