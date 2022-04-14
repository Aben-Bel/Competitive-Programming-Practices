class Solution {
    public int findMin(int[] nums) {
        if(nums.length ==1 || nums[0]<nums[nums.length-1]) return nums[0];
        
        int left=0,right=nums.length-1,mid=0;
        int best = -1;
        while(left<=right){
            mid = left + (right-left)/2;
            if(nums[0]>nums[mid]){
                best = nums[mid];
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return best;
    }
}