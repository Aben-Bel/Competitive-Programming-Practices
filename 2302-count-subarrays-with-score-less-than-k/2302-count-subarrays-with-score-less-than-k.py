class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0 
        _sum = 0
        count = 0
        for right in range(len(nums)):
            _sum += nums[right]
            while _sum*(right - left + 1) >= k:
                _sum -= nums[left]
                left+=1
            
            count += (right - left + 1)
        
        return count