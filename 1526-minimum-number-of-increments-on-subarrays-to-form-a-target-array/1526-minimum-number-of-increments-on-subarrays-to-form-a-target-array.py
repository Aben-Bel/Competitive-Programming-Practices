class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # [1,2,3,4,2,1]
        # [1,2,3,4]
        
        stack = []
        ans = target[0]
        for i in range(0, len(target)):
            while stack and stack[-1] < target[i]:
                prev = stack.pop()
                ans += (target[i] - prev)
                stack.clear()
            stack.append(target[i])
        return ans