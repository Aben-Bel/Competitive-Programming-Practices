class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*(len(nums1)+1) for i in range(len(nums2)+1)]
        m = 0
        for i in range(len(nums1)-1,-1,-1):
            for j in range(len(nums2)-1,-1,-1):
                if nums1[i] == nums2[j]:
                    dp[j][i] = dp[j+1][i+1]+1
                   
        return max(max(row) for row in dp)