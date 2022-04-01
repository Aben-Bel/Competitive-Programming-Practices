class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<String, Integer> map = new HashMap<>();
        int left = 0, right = 0, max = 0;
        int ck = k;
        
        while(right<s.length()){
            String rs = s.charAt(right)+"";
            String ls = s.charAt(left)+"";
            map.put(rs, map.getOrDefault(rs, 0) + 1);
            max = Math.max(max, map.getOrDefault(rs, 0));
            if(right-left - max < k){
                right++;
            }else{
                map.put(ls, map.get(ls)-1);
                left++;
                right++;
            }
        }
        
        return right - left;
        
    }
}