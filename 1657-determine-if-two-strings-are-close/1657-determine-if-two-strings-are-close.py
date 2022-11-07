class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1Counter = Counter(word1)
        word2Counter = Counter(word2)
        
        return all([key in word2Counter for key in word1Counter]) and sorted(word2Counter.values()) == sorted(word1Counter.values())
        
        