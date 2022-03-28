class Solution {
    public int[] countBits(int n) {
        int[] res = new int[n+1];
        for(int i=0;i<=n;i++){
            res[i] = count(i);
        }
        return res;
    }
    
    public int count(int n){
        int count = 0;
        while(n>0){
            count+=1;
            n = n&(n-1);
        }
        return count;
    }
}