class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # 000
        # 001
        # 010
        # 011
        # 100
        # 101
        # 110
        # 111 -> 7
        result = []
        for i in range(2**(n)):
            mask = i
            temp = []
            j = 0
            while mask>0:
                if mask&1 == 1:
                    temp.append(nums[j])
                mask >>= 1
                j+=1
            
            result.append(temp)
        return result
                