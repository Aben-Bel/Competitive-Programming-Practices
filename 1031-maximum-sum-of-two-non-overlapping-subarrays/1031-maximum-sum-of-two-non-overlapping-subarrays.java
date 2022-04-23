class Solution {
    int[] pre;
    int firstLen;
    int secondLen;
    int[][][] dp;
    public int maxSumTwoNoOverlap(int[] nums, int firstLen, int secondLen) {
        this.firstLen = firstLen;
        this.secondLen = secondLen;
        dp = new int[nums.length][2][2];
        for(int i=0;i<nums.length;i++){
            for(int j=0;j<2;j++){
                for(int k=0;k<2;k++){
                    dp[i][j][k] = -1;
                }
            }
        }
        
        pre = new int[nums.length+1];
        pre[0] = 0;
        for(int i=0;i<nums.length;i++){
            pre[i+1] += nums[i] + pre[i]; 
        }
        
        return max(0,0,0);
    }
    
    public int max(int i, int first,int second){
        if(first==1 && second==1){
            return 0;
        }
        
        if(i>=pre.length-1){
            return 0;
        }
        
        if(dp[i][first][second]!=-1) return dp[i][first][second];
        
        int choice1 = max(i+1, first, second);
        int choice2 = 0;
        if(first==0 && i+firstLen < pre.length) choice2 = pre[i+firstLen] - pre[i] + max(i+firstLen, 1, second);
        int choice3 = 0;
        if(second==0 && i+secondLen < pre.length)choice3 = pre[i+secondLen] - pre[i] + max(i+secondLen, first, 1);
        
        
        dp[i][first][second] =  Math.max(choice1, Math.max(choice2, choice3));
        return dp[i][first][second];
    }
}