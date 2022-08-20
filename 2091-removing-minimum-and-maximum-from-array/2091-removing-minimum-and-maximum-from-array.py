class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        _min = float('inf')
        _max = float('-inf')
        _min_index = -1
        _max_index = -1
        for i in range(len(nums)):
            num = nums[i]
            if _min > num:
                _min = num
                _min_index = i
            if _max < num:
                _max = num
                _max_index = i

        small = min(_max_index, _min_index)+1
        mid = abs(_max_index - _min_index)
        left = small + mid
        right = len(nums)-small+1
        
        return min(len(nums)-mid+1,left,right)