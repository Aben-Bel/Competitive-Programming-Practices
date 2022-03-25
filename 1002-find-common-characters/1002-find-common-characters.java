class Solution {
    int[] dic;
    public List<String> commonChars(String[] words) {
        dic = new int[26];
        String previous = words[0];
        for(int i=1;i<words.length;i++){
            String current = "";
            dic = createDic(previous);
            for(char c : words[i].toCharArray()){
                if(dic[c-'a']>0){
                    current += c;
                    dic[c-'a']--;
                }
            }
            previous = current;
        }
        List<String> result = Arrays.asList(previous.split(""));
        if(result.size()==1 && result.get(0).equals("")) return new ArrayList<>();
        return result;
    }
    
    public int[] createDic(String s){
        dic = new int[26];
        for(char c : s.toCharArray()){
            dic[c-'a']++;
        }
        return dic;
    }
}