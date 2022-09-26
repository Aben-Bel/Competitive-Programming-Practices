class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:     
        one = two = float('inf')
        
        for num in nums:
            if one > num:
                one = num
            
            if two > num and one < num:
                two = num
            
            if two < num:
                return True
        
        return False