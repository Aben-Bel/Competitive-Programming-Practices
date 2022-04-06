class Solution {
    int[][] rides;
    HashMap<Integer, Long> mem = new HashMap<>();
    public long maxTaxiEarnings(int n, int[][] rides) {
        this.rides = rides;
        Arrays.sort(rides, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return Integer.compare(a[0], b[0]);
            }
        });
        
        return dp(0);
    }
    
    public int binarySearchEnd(int i){
        int left = 0, right = rides.length - 1, mid = 0;
        int best = -1;
        while(left<=right){
            mid = left + (right-left)/2;
            if(rides[mid][0] >= i){
                best = mid;
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return best;
    }
    
    public long dp(int i){
        if(i==-1 || i>=rides.length) {
            return 0;
        }
        if(mem.containsKey(i)) return mem.get(i);
        
        int ni = binarySearchEnd(rides[i][1]);
        long take = rides[i][1]-rides[i][0] + rides[i][2] + dp(ni);
        long skip = dp(i+1);
        
        mem.put(i, Math.max(take, skip));
        return mem.get(i);
    }
}