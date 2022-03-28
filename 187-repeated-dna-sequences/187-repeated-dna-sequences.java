class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        HashMap<String, Integer> tenLongStrings = new HashMap<String, Integer>();
        
        for(int i=0;i<=s.length()-10;i++){
            String val = s.substring(i,i+10);
            tenLongStrings.put(val, tenLongStrings.getOrDefault(val, 0) + 1);
        }
        List<String> result = new ArrayList<>();
        for(Map.Entry<String, Integer> entry : tenLongStrings.entrySet()){
            if(entry.getValue() > 1){
                result.add(entry.getKey());
            }
        }
        return result;
    }
}