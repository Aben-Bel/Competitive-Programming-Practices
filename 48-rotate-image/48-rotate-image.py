class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i != j and i <j:
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
        for i in range(len(mat)):
            left = 0
            right = len(mat[i])-1
            while left<right:
                mat[i][left], mat[i][right] = mat[i][right], mat[i][left]
                left += 1
                right -= 1
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    