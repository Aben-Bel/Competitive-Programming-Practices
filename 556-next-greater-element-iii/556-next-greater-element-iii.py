class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        1. Find the first smallest place you can swap with some greater place
        2. Find a place to swap the one you find at step 1
        3. Swap the two from 1. and 2.
        4. then sort everything to the right from the 1. to make it the smallest
        """
        if n == 2**31-1:
            return -1
        
        nums = list(str(n))
        #120765
        smallest_place = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i]  < nums[i+1]:
                smallest_place = i
                break
        if smallest_place == -1: return -1
        swap_place= -1
        for i in range(len(nums)-1,smallest_place,-1):
            if nums[i] > nums[smallest_place]:
                swap_place = i
                break
                
        nums[swap_place], nums[smallest_place] = nums[smallest_place], nums[swap_place]
        left = smallest_place+1
        right = len(nums)-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            right-=1
            left+=1
        
        res=  int("".join(nums))
        if res == n or res > 2**31-1:
            return -1
        return res
        
        
        