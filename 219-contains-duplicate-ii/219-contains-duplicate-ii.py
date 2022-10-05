class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        val = {}
        for i in range(len(nums)):
            if nums[i] in val:
                if abs(i-val[nums[i]]) <= k:
                    return True
            val[nums[i]] = i
        return False