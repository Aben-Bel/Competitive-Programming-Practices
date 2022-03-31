class Solution {
    int NRow;
    List<List<Integer>> triangle;
    int[][] memo;
    
    public int minimumTotal(List<List<Integer>> traingle) {
        this.triangle = traingle;
        NRow = this.triangle.size();
        memo = new int[NRow][NRow];
        for(int[] row : memo){
            Arrays.fill(row,100000);
        }
        return Math.min(tri(0,0), tri(0,1));
    }
    
    public int tri(int row, int col){
        if(col>=triangle.get(row).size()) return 100000;
        if(memo[row][col]!=100000) return memo[row][col];
        if(row == NRow-1){
            return triangle.get(row).get(col);   
        }
        
        int result = triangle.get(row).get(col) + Math.min(tri(row+1, col), tri(row+1, col+1));
        memo[row][col] = result;
        return result;
    }
}