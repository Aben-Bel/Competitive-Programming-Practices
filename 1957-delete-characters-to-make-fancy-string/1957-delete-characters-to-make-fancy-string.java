class Solution {
    public String makeFancyString(String s) {
        int i=0;
        StringBuilder res = new StringBuilder("");
        while(i<s.length()){
            if(i+2<s.length() && s.charAt(i) == s.charAt(i+1) && s.charAt(i+1) == s.charAt(i+2)){
                i+=1;
                continue;
            }
            res.append(s.charAt(i));
            i+=1;
        }
        return res.toString();
    }
}