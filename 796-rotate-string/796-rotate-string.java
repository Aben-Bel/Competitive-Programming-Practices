class Solution {
    public boolean rotateString(String s, String goal) {
        if(s.length() != goal.length()) return false;
        String x = goal + goal;
        int l = s.length();
        for(int i=0;i<=x.length() - l;i++){
            if(x.substring(i,i+l).equals(s)) return true;
        }
        return false;
    }
}