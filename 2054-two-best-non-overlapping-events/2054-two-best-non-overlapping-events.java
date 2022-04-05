class Solution {
    int[][] events;
    int[][] dp;
    public int maxTwoEvents(int[][] events) {
        this.events = events;
        dp = new int[events.length][3];
        Arrays.sort(events, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return Integer.compare(a[0], b[0]);
            }
        });
        
        return dp(0,2);
    }
    
    public int binarySearchEnd(int i){
        int left = 0, right = events.length - 1, mid = 0;
        int best = -1;
        while(left<=right){
            mid = left + (right-left)/2;
            if(events[mid][0] > i){
                best = mid;
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return best;
    }
    
    public int dp(int i, int canTake){
        if(canTake == 0) return 0;
        if(i==-1 || i>=events.length) {
            return 0;
        }
        if(dp[i][canTake]!=0) return dp[i][canTake];
        int ni = binarySearchEnd(events[i][1]);
        
        int res1=0,res2=0;

        res1 = events[i][2] + dp(ni, canTake-1);
        res2 = dp(i+1, canTake);
        dp[i][canTake] = Math.max(res1, res2);
        return dp[i][canTake];
    }
}