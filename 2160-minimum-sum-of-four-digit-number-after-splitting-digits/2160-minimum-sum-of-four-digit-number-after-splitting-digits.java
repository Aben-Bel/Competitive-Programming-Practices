class Solution {
    public int minimumSum(int num) {
        String s = "" + num;
        char[] sc = s.toCharArray();
        Arrays.sort(sc);
        s = new String(sc);
        String s1 = "";
        String s2 = "";
        int l = 0, r=1;
        while(r<s.length()){
            s1 += s.charAt(l);
            s2 += s.charAt(r);
            l+=2;
            r+=2;
        }
        return Integer.parseInt(s1) + Integer.parseInt(s2);
    }
}