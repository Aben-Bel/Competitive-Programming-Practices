class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        containsOne = False
        for i in range(n):
            if nums[i] == 1:
                containsOne = True
            if nums[i] > n:
                nums[i] = 1
            if nums[i] <= 0:
                nums[i] = 1
        
        if not containsOne:
            return 1
        
        for i in range(n):
            val = abs(nums[i])
            if val == n:
                nums[0] = - abs(nums[0])
            else:
                nums[val] = - abs(nums[val])
        
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return n
        
        return n + 1
        
        
        
        
        