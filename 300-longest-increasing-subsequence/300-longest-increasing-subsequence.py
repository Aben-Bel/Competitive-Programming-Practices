class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def search(seq, val):
            left = 0
            right = len(seq) - 1
            best = len(seq)
            while left <= right:
                mid = (left + right)//2
                if seq[mid] >= val:
                    best = mid
                    right = mid - 1
                else:
                    left = mid + 1
                    
            return best
        
        seq = []
        for i in range(len(nums)):
            j = search(seq, nums[i])
            if j == len(seq):
                seq.append(nums[i])
            else:
                seq[j] = nums[i]
        
        return len(seq)