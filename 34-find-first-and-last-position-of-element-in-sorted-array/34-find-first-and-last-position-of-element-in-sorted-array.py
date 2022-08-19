class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        best1 = -1
        left = 0
        right = len(nums)-1
        
        while left<=right:
            mid = (left+right)//2
            if nums[mid] <= target:
                best1 = mid
                left = mid + 1
            else:
                right = mid - 1
        best2 = -1
        
        left = 0
        right = len(nums) - 1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] >= target:
                best2 = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if best1 != -1 and  nums[best1] != target:
            best1 = -1
        if best2!=-1 and nums[best2] != target:
            best2 = -1
        return [best2,best1]