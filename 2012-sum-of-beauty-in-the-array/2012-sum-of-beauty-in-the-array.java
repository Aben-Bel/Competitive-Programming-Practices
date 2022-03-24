class Solution {
    public int sumOfBeauties(int[] nums) {
        int[] maxes = new int[nums.length];
        int[] mins = new int[nums.length];
        int n = nums.length;
        maxes[0] = nums[0];
        mins[nums.length-1] = nums[nums.length-1];
        for(int i=1;i<nums.length;i++){
            maxes[i] = Math.max(maxes[i-1], nums[i]);
            mins[n-1-i]=Math.min(mins[n-i], nums[n-1-i]);
        }
        
        int count = 0;
        for(int i=1;i<nums.length-1;i++){
            if(nums[i]>maxes[i-1] && nums[i]<mins[i+1]){
                count+=2;
            }else if(nums[i-1]<nums[i] && nums[i]<nums[i+1]){
                count+=1;
            }
        }
        
        return count;
        
    }
}