class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap1 = {}
        for num in nums1:
            hashmap1[num] = 1
            
        result = {}
        for num in nums2:
            if num in hashmap1:
                result[num] = 1
                
        return list(result.keys())