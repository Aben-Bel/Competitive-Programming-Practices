class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = 2**(len(nums[0]))
        k = len(nums[0])
        nums = [ int(num, 2) for num in nums]
        def ans(nums):
            def cyclicSort():
                i = 0
                while i<len(nums):
                    correct = nums[i]
                    if 0 <= nums[i] < len(nums) and nums[correct] != nums[i]:
                        nums[correct], nums[i] = nums[i],nums[correct]
                    else:
                        i+=1

            cyclicSort()
            for i, val in enumerate(nums):
                if i != val:
                    return i
            return len(nums)
        
        result = bin(ans(nums))[2:]
        
        return (k-len(result))*"0" + result