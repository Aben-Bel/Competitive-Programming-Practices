class Solution:
    def customSortString(self, order: str, s: str) -> str:
        index = -len(s)
        orderTable = defaultdict(int)
        for char in order:
            orderTable[char] = index
            index+=1
        
        s = "".join(sorted(list(s),key=lambda x : orderTable[x]))
        return s