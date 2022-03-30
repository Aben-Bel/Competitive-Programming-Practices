class Solution {
    public String makeFancyString(String s) {
        int i=0;
        StringBuilder res = new StringBuilder(s);
        
        while(i+2<res.length()){
            if(res.charAt(i) == res.charAt(i+1) && res.charAt(i+1) == res.charAt(i+2)){
                res.deleteCharAt(i);
                continue;
            }
            i+=1;
        }
        return res.toString();
    }
}