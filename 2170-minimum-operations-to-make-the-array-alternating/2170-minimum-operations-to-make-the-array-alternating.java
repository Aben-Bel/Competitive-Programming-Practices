class Solution {
    public int minimumOperations(int[] nums) {
        if(nums.length == 1) return 0;
        HashMap<Integer, Integer> odd = new HashMap<>();
        HashMap<Integer, Integer> even = new HashMap<>();
        
        for(int i=0;i<nums.length;i+=2){
            even.put(nums[i], even.getOrDefault(nums[i], 0)+1);
        }
        
        for(int i=1;i<nums.length;i+=2){
            odd.put(nums[i], odd.getOrDefault(nums[i], 0)+1);
        }
        
        int e = 0, o = 0;
        int po=0;
        int pe=0;
        int oVal =0;
        int eVal =0;
        
        for(Map.Entry<Integer, Integer> entry : even.entrySet()){
            if(e<=entry.getValue()){
                pe = e;
                e = entry.getValue();
                eVal = entry.getKey();
            }else if(pe<=entry.getValue()){
                pe=entry.getValue();
            }
        }
        
        for(Map.Entry<Integer, Integer> entry : odd.entrySet()){
            if(o<=entry.getValue()){
                po = o;
                o = entry.getValue();
                oVal = entry.getKey();
            }else if(po<=entry.getValue()){
                po=entry.getValue();
            }
        }
        
        
        if(eVal!=oVal) return nums.length - (e+o);
        
        return Math.min(nums.length - (e+po),nums.length - (o+pe));
        
    }
}