class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        res = []
        start = 0
        while start < len(intervals) and intervals[start][1] < newInterval[0]:
            res.append(intervals[start])
            start+=1
        
        if res and res[-1][1] >= newInterval[0]:
            res[-1] = [min(res[-1][0], newInterval[0]), max(res[-1][1], newInterval[1])]
        else:
            res.append(newInterval)
            
        end = start
        for end in range(start, len(intervals)):
            if res[-1][1] >= intervals[end][0]:
                 res[-1] = [min(res[-1][0], intervals[end][0]), max(res[-1][1], intervals[end][1])]
            else:
                res.append(intervals[end])
        
        return res