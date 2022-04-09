class Solution {
    public int[] sumZero(int n) {
        int neg = n/2;
        int pos = n - neg;
        int[] res = new int[n];
        int sum = 0;
        int j = 0;
        for(int i=0;i<pos;i++){
            res[i] = i+1;
            sum+=res[i];
            j=i;
        }
        // 1, 2, 3, -1, -2
        for(int i=0;i<neg;i++){
            res[j+1+i] = -(i+1);
            sum+=res[j+1+i];
        }
        
        res[n-1] -= sum;
        return res;
        
    }
}