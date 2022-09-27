class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:    
        if len(nums) < 3:
            return False
        
        def getIndex(val, triplets):
            left = 0
            right = len(triplets) -1
            best = -1
            while left <= right:
                mid = (left + right)//2
                if triplets[mid]  > val:
                    best = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if best!=-1 and val != triplets[best-1]: return best
            return -1
        
        triplets = [nums[0]]
        for i in range(1, len(nums)):
            if triplets[-1] < nums[i]:
                triplets.append(nums[i])
                if len(triplets) == 3:
                    return True
            else:
                j = getIndex(nums[i], triplets)
                if j != -1: triplets[j] = nums[i]
        return False
                