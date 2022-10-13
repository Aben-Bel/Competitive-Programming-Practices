class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        res = 0
        # [1,1,1,0,0,0,1,1,1,1,0], k = -1
        #          l
        #                        r
        while l<=r and r<len(nums):
            if nums[r] == 1 and k>=0:
                r+=1
            elif k>=0:
                r+=1
                k-=1
            else:
                if nums[l] == 0:k+=1
                l+=1
            if k>=0:
                res = max(res, r-l)
        return res
                