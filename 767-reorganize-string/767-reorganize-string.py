class Solution:
    def reorganizeString(self, s: str) -> str:
        d = Counter(s)
        heap = []
        for key in d:
            heapq.heappush(heap, (-d[key], key))
        
        res = []
        while len(heap)>1:
            ff, fc = heapq.heappop(heap)
            sf, sc = heapq.heappop(heap)
            
            ff, sf= (-1)*ff, (-1)*sf
            
            res.append(fc)
            res.append(sc)
            if ff - 1 > 0:
                ff-=1
                heapq.heappush(heap, (ff*(-1),fc))
            
            if sf - 1 > 0:
                sf-=1
                heapq.heappush(heap, (sf*(-1),sc))
            
        if len(heap) > 0:
            ff, fc = heapq.heappop(heap)
            if (-1)*ff > 1:
                return ""
            
            return "".join(res) + fc
        return "".join(res)
            
            
            