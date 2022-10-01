class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        c = Counter(barcodes)
        
        res = [0]*len(barcodes)
        i = 0
        for k, v in c.most_common():
            for _ in range(v):
                res[i] = k
                i+=2
                if i>=len(barcodes):
                    i=1
        
        return res