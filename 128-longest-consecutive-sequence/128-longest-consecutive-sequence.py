class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        length = 1
        checked = set()
        for num in nums:
            if num + 1 in num_set and num + 1 not in checked:
                count = 1
                val = num+1
                while val in num_set:
                    checked.add(val)
                    count += 1
                    val = val+1
                val = num-1
                while val in num_set:
                    checked.add(val)
                    count += 1
                    val = val-1
                length = max(length, count)
        
        return length
                