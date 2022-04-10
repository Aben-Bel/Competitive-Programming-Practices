class Solution {
    public int maximumProduct(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>();
        for(int num : nums){
            heap.offer(num);
        }
        
        while(k>0){
            int cur = heap.remove();
            cur+=1;
            heap.offer(cur);
            k-=1;
        }
        
        long result = 1;
        while(!heap.isEmpty()){
            result *= (heap.remove()%1000000007);
            result %= 1000000007;
        }
        return (int)result%1000000007;
    }
}