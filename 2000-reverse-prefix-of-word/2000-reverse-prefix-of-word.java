class Solution {
    public String reversePrefix(String word, char ch) {
        int i = 0;
        while(i<word.length()){
            if(word.charAt(i)==ch) break;
            i+=1;
        }
        
        if(i==word.length() || word.charAt(i) != ch) return word;
        
        int left = 0, right = i;
        StringBuilder sb = new StringBuilder(word);
        while(left<right){
            char temp = sb.charAt(right);
            sb.replace(right, right+1, "" + sb.charAt(left));
            sb.replace(left, left+1, "" + temp);
            left++;
            right--;
        }
        
        return sb.toString();
    }
}