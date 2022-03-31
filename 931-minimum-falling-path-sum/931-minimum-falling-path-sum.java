class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int nRow = matrix.length;
        int nCol = matrix[0].length;
        int min = Integer.MAX_VALUE;
        for(int row=1;row<nRow;row++){
            for(int col=0;col<nCol;col++){
                int top = col;
                int topLeft = col-1;
                int topRight = col+1;
                int res = Integer.MAX_VALUE;
                res = Math.min(res, matrix[row-1][top]);
                if(topLeft >= 0) res = Math.min(res, matrix[row-1][topLeft]);
                if(topRight < nCol) res = Math.min(res, matrix[row-1][topRight]);
                matrix[row][col] = res + matrix[row][col];
            }
        }
        
        for(int col=0;col<nCol;col++){
            min = Math.min(matrix[nRow-1][col], min);
        }
        return min;
    }
}