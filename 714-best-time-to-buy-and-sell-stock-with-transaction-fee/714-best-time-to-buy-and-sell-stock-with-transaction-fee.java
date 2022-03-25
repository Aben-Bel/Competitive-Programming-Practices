class Solution {
    int fee;
    int prices[];
    int[][] mem;
    public int maxProfit(int[] prices, int fee) {
        this.fee = fee;
        this.prices = prices;
        mem = new int[prices.length][2];
        for(int[] a : mem){
            Arrays.fill(a, -1);
        }
        return dp(0,0);
    }
    
    public int dp(int i, int holding){
        if(i>=prices.length) return 0;
        if(mem[i][holding]!=-1) return mem[i][holding];
        
        int res;
        if(holding == 1){
            int sale = prices[i] + dp(i+1,0) - fee;
            int nothing = dp(i+1,holding);
            res = Math.max(sale, nothing);
        }else{
            int buy = -prices[i] + dp(i+1,1);
            int nothing = dp(i+1,holding);
            res = Math.max(buy, nothing);
        }
        mem[i][holding] = res;
        return res;
    }
}