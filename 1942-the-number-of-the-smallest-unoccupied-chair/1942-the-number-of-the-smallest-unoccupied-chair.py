class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        cur = [0]
        intervals = []
        for i in range(len(times)):
            intervals.append((times[i][0],1,i))
            intervals.append((times[i][1],-1,i))
        
        seat = {}
        intervals.sort()
        for i in range(len(intervals)):
            t, drop, person = intervals[i]
            if drop == 1:
                if len(cur)==1:
                    heapq.heappush(cur, cur[-1]+1)     
                seat[person] = heapq.heappop(cur)
                if person == targetFriend:
                    return seat[person]
            else:
                heapq.heappush(cur, seat[person])
        return -1