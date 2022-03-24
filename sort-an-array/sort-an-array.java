class Solution {
    public int[] sortArray(int[] nums) {
        if(nums.length<2) return nums;
        
        int mid = nums.length/2;
        int[] leftNums = sortArray(Arrays.copyOfRange(nums, 0, mid));
        int[] rightNums = sortArray(Arrays.copyOfRange(nums, mid, nums.length));
        
        int[] res = new int[leftNums.length + rightNums.length];
        
        int fc = 0, lc=0,rc=0;
        while(lc<leftNums.length && rc<rightNums.length){
            if(leftNums[lc] < rightNums[rc]){
                res[fc] = leftNums[lc];
                lc++;
            }else{
                res[fc] = rightNums[rc];
                rc++;
            }
            fc++;
        }
        
        while(lc<leftNums.length){
            res[fc] = leftNums[lc];
            fc++;lc++;
        }
        
        while(rc<rightNums.length){
            res[fc] = rightNums[rc];
            fc++;rc++;
        }
        
        return res;
    }
}