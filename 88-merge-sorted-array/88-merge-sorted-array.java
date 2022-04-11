class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] res = new int[n+m];
        
        int l1 =0,l2=0,i=0;
        while(l1<m && l2<n){
            if(nums1[l1]<nums2[l2]){
                res[i++] = nums1[l1++];
            }else{
                res[i++] = nums2[l2++];
            }
        }
        
        while(l1<m){
            res[i++] = nums1[l1++];
        }
        
        while(l2<n){
            res[i++] = nums2[l2++];
        }
        
        for(int j=0;j<nums1.length;j++){
            nums1[j]=res[j];
        }
        
    }
}