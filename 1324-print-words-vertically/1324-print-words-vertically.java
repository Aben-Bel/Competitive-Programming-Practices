class Solution {
    public List<String> printVertically(String s) {
        String[] words = s.split(" ");
        int max = 0;
        for(String word : words){
            max = Math.max(word.length(), max);
        }
        int ith=0;
        List<String> result = new ArrayList<>();
        while(max>0){
            for(String word : words){
                if(result.size() <= ith){
                    if(word.length() <= ith) result.add(" ");
                    else result.add(word.charAt(ith) + "");
                }else{
                    if(word.length() <= ith) result.set(ith, result.get(ith) + " ");
                    else result.set(ith, result.get(ith)+word.charAt(ith));
                }
            }
            ith+=1;
            max-=1;
        }
        for(int i=0;i<result.size();i++){
            result.set(i, rtrim(result.get(i)));
        }
        return result;
    }
    
    public static String rtrim(String s) {
        int i = s.length()-1;
        while (i >= 0 && Character.isWhitespace(s.charAt(i))) {
            i--;
        }
        return s.substring(0,i+1);
    }
}