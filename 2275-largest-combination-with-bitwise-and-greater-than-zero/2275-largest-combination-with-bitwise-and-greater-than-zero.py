class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_count = 0
        for i in range(max(candidates).bit_length()):
            count=0
            for i in range(len(candidates)):
                count += (candidates[i]&1)
                candidates[i] >>= 1
            max_count = max(max_count, count)
        
        return max_count
        