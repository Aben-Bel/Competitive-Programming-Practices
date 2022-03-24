class Solution {
    public int sumOfBeauties(int[] nums) {
        int[] maxes = new int[nums.length];
        int[] mins = new int[nums.length];
        
        maxes[0] = nums[0];
        for(int i=1;i<nums.length;i++){
            maxes[i] = Math.max(maxes[i-1], nums[i]);
        }
        mins[nums.length-1] = nums[nums.length-1];
        for(int i=nums.length-2;i>=0;i--){
            mins[i] = Math.min(mins[i+1], nums[i]);
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