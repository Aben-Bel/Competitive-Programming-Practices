class Solution {
    public List<Integer> partitionLabels(String s) {
        int[] occurLast = new int[26];
        for(int i=0;i<s.length();i++){
            occurLast[s.charAt(i)-'a'] = i;
        }
        
        int j=0,anchor = 0;
        List<Integer> ans = new ArrayList<>();
        for(int i=0;i<s.length();i++){
            j = Math.max(j, occurLast[s.charAt(i)-'a']);
            if(i==j){
                ans.add(i-anchor+1);
                anchor = i + 1;
            }
        }
        return ans;
    }
}