class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def generate(picked, path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if i not in picked:
                    picked.add(i)
                    path.append(nums[i])
                    generate(picked, path)
                    picked.remove(i)
                    path.pop()
        generate(set(), [])
        return result