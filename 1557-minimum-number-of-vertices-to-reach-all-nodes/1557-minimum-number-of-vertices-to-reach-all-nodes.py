class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inDegree = defaultdict(int)
        for edge in edges:
            inDegree[edge[1]] += 1
            inDegree[edge[0]] += 0
            
        result = set()
        for key in inDegree:
            if inDegree[key] == 0:
                result.add(key)
        return result
        