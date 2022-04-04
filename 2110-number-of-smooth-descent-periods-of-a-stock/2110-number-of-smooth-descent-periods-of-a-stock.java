class Solution {
    public long getDescentPeriods(int[] prices) {
        long count = 0;
        int left = 0, right = 0;
        while(right<prices.length){
            if(right==prices.length-1 || prices[right] != prices[right+1]+1){
                long n = right - left + 1;
                count += ((n*(n+1))/2);
                left = right+1;
            }
            right+=1;
        }
        return count;
    }
}