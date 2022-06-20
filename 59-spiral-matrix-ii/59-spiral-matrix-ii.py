class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        cur = 0
        result = [[0]*n for i in range(n)]
        
        count = 1
        while count <= n*n:
            for i in range(cur, n-cur):
                result[cur][i] = count
                count += 1
            
            for i in range(cur+1, n-cur):
                result[i][n-cur-1] = count
                count += 1
            
            for i in range(n-cur-2,cur-1,-1):
                result[n-cur-1][i] = count
                count += 1
            
            for i in range(n-cur-2,cur,-1):
                result[i][cur] = count
                count += 1
            
            cur += 1
            
        return result