class Solution {
    public int minimumBuckets(String sb) {
        int countH = 1;
        int count = 0;
        sb = "H" + sb + "H";
        StringBuilder street = new StringBuilder(sb);
        int n = street.length();
        for(int i=1;i<n-1;i++){
            if(street.charAt(i)!='H' || street.charAt(i+1) == 'B' || street.charAt(i-1) == 'B'){
                continue;
            }
            
            if(street.charAt(i+1)=='.'){
                street.setCharAt(i+1, 'B');
                count+=1;
            }else if(street.charAt(i-1) == '.'){
                street.setCharAt(i-1, 'B');
                count+=1;
            }else{
                return -1;
            }
        }
        // System.out.println(street.toString());
        
        return count;
    }
}