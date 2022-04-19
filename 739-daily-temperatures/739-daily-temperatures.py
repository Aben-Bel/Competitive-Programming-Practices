class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        stack.append((0,temperatures[0]))
        
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                cur = stack.pop()
                result[cur[0]] = i - cur[0]
            stack.append((i,temperatures[i]))
                
        return result