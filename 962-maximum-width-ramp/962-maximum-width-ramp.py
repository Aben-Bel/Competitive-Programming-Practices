class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, a in enumerate(nums):
            if not stack or nums[stack[-1]] > a:
                stack.append(i)
        
        m = 0
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                m = max(m, i - stack.pop())
        
        return m