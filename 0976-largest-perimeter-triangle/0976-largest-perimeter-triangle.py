class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        best = 0
        ptr1 = 0
        ptr2 = 1
        ptr3 = 2
        
        while ptr3<len(nums):
            if nums[ptr3] >= nums[ptr2] + nums[ptr1]:
                if ptr2+1<ptr3:
                    ptr2+=1
                elif ptr2 == ptr3-1 and ptr1+1<ptr2:
                    ptr1+=1
                else:
                    ptr3 += 1
            else:
                best = nums[ptr1] + nums[ptr2] + nums[ptr3]
                if ptr2+1<ptr3:
                    ptr2+=1
                elif ptr1+1<ptr2:
                    ptr1+=1
                else:
                    ptr3+=1
        
        return best
    
        
        