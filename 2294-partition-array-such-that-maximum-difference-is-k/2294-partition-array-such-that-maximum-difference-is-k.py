class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        #  nums = [3,6,1,2,5], k = 2
        maximum = -1 - k
        minimum = 1000000
        nums.sort()
        count = 1
        for num in nums:
            maximum = max(maximum, num)
            minimum = min(minimum, num)
            
            if maximum - minimum > k:
                count += 1
                maximum = minimum = num
        return count
        
        