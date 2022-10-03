class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        matrix = [[float('inf') if i!=j else 0 for j in range(n)] for i in range(n)]
        
        for a,b,w in times:
            matrix[a-1][b-1] = w
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                for l in range(n):
                    matrix[j][l] = min(matrix[j][l], matrix[j][i]+matrix[i][l])
        res = max(matrix[k-1])
        return res if res!=float('inf') else -1
        
        
            