class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # items=[[1,2],[3,2],[2,4],[5,6],[3,5]]
        # sorti=[[1,2],[2,4],[3,2],[3,5],[5,6]]
        # prefi=[  2  ,  4  ,  4  ,  5  ,  6  ]
        # queri=[  1  ,  2  ,  3  ,  4  ,  5 ,  6]
        items.sort()
        prefix = []
        runningMax = items[0][1]
        for i in range(len(items)):
            runningMax = max(runningMax, items[i][1])
            prefix.append(runningMax)
        
        def search(val, items):
            left = 0
            right = len(items)-1
            best = -1
            while left<=right:
                mid = (left+right)//2
                if items[mid][0] <= val:
                    best = mid
                    left = mid + 1
                else:
                    right = mid - 1
            
            return best 
        ans = []
        for query in queries:
            find = search(query,items)
            if find != -1: 
                ans.append(prefix[find])
            else:
                ans.append(0)
        return ans
        
        