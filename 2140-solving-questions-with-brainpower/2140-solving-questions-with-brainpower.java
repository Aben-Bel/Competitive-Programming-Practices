class Solution {
    int[][] questions;
    long[] memo;
    public long mostPoints(int[][] questions) {
        this.questions = questions;
        memo = new long[questions.length];
        return dp(0);
    }
    
    public long dp(int i){
        if(i>=questions.length) return 0;
        if(memo[i]!=0) return memo[i];
        
        long pickMe = questions[i][0] + dp(i+questions[i][1]+1);
        long dontPickMe = dp(i+1);
        
        memo[i] = Math.max(pickMe, dontPickMe);
        return memo[i];
    }
}