class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if(numRows == 1):
            return [[1]]
    
        pascal = [[1],[1,1]]
        for i in range(2, numRows):
            arr = [1]*(i+1)
            pascal.append(arr)
            for j in range(i+1):
                if i > 1 and  j>0 and j < len(pascal[i-1]):
                    pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]
        return pascal