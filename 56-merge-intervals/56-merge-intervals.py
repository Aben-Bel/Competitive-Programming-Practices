class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        tuples = []
        for interval in intervals:
            tuples.append((interval[0], 1))
            tuples.append((interval[1]+1, -1))
        
        tuples.sort()
        presum = 0
        start = tuples[0][0]
        ans = []
        for i in range(len(tuples)):
            if presum == 0:
                start = tuples[i][0]
            presum+= tuples[i][1]
            if presum == 0:
                ans.append([start, tuples[i][0]-1])
        return ans