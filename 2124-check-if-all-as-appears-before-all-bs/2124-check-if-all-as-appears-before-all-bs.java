class Solution {
    public boolean checkString(String s) {
        boolean result = false;
        for(char c : s.toCharArray()){
            if(c=='b'){
                result=true;
            }else if(c=='a' && result==true){
                return false;
            }else{
                result = false;
            }
        }
        if(s.charAt(s.length()-1) == 'a' && result == false) return true;
        return result;
    }
}