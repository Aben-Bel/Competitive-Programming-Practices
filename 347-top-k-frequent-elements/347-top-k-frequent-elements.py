class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        
        freq = [[] for i in range(len(nums)+1)]
        
        for n, c in c.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1,-1,-1):
            for j in range(len(freq[i])):
                if len(res) < k:
                    res.append(freq[i][j])
                else:
                    return res
        return res