class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canWeFill(guess, piles):
            hours = 0
            for pile in piles:
                hours += ceil(pile/guess)
            return hours
        
        left = 1
        right = max(piles)
        best = -1
        while left<=right:
            mid = (right+left)//2
            
            if h>=canWeFill(mid, piles):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return best
        
        
            