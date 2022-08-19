class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def countLess(nums, x):
            count = 0
            for i in range(len(nums)):
                if nums[i] <= x:
                    count += 1
            return count
        
        
        left = 0
        right = len(nums)-1
        best = -1
        while left<=right:
            mid = (left+right)//2
            
            if countLess(nums,mid) > mid:
                best = mid
                right = mid-1
            else:
                left = mid+1
        return best