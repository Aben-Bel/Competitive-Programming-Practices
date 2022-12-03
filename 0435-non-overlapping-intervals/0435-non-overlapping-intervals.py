class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda a : (a[1],a[0]))
        print(intervals)
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1] > intervals[i][0]:
                continue
            res.append(intervals[i])
        
        return len(intervals) - len(res)
            