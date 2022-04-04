class Solution {
    public long countVowels(String word) {
        HashSet<String> vowels = new HashSet<>();
        vowels.add("a");vowels.add("e");vowels.add("i");vowels.add("o");vowels.add("u");
        long n = word.length();
        
        long result = 0;
        for(int i=0;i<n;i++){
            if(vowels.contains(word.charAt(i)+""))
                result = (result + n + i*(n-i-1));
        }
        
        return result;
    }
}