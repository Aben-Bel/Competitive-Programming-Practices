class Solution {
    int[][] mem;
    int n;
    public int numWays(int steps, int arrLen) {
        mem = new int[(int)(steps/2+1)][steps+1];
        n = arrLen;
        for(int[] a : mem){
            Arrays.fill(a, -1);
        }
        return dp(steps, 0);
    }
    
    public int dp(int steps, int i){
        if(i==0 && steps == 0) return 1;
        
        if(i<0 || i>=n || i>=mem.length || i>steps || steps <= 0 || steps>=mem[0].length) return 0;
        
        if(mem[i][steps] != -1) return mem[i][steps];
        
        int res = ((dp(steps-1, i-1) + dp(steps-1,i+1))%1000000007 + dp(steps-1,i))%1000000007;
        mem[i][steps] = res;
        return res;
    }
}