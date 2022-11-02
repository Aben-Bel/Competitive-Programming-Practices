class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # [2,3,-1,8,4]
        #  0,2, 5,4,8
        # 17 15 12 8 0
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        
        for i in range(len(nums)):
            if prefix[i] == (prefix[-1] - prefix[i+1]):
                return i
        
        return -1
            
        
            