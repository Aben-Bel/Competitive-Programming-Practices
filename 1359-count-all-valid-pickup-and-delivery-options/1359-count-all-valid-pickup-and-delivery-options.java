class Solution {
    long[][] memo;
    public int countOrders(int n) {
        memo=new long[n+1][n+1];
        return (int)count(n,n);
    }
    
    public long count(int unpicked, int undelivered){
        if(unpicked == 0 && undelivered == 0){
            return 1;
        }
        
        if(unpicked <0 || undelivered < 0 || undelivered < unpicked){
            return 0;
        }
        
        if(memo[unpicked][undelivered]!=0){
            return memo[unpicked][undelivered];
        }
        
        long result = 0;
        result += unpicked * count(unpicked-1, undelivered) % 1000000007;
        result += (undelivered - unpicked) * count(unpicked, undelivered - 1) % 1000000007;
        
        memo[unpicked][undelivered] = result;
        return result;
    }
}