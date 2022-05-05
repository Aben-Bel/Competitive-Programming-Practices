class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        suffix = {}
        num_hashes = 0
        countMergedWords = 0
        for word in words:
            self.addWord(suffix, word[::-1])
        
        usedWords = set()
        for word in words:
            if not self.isSuffix(suffix, word[::-1]):
                if word not in usedWords:
                    num_hashes += 1
                    usedWords.add(word)
        
        return num_hashes + sum(map(len,usedWords)) 
        
    def addWord(self, suffix, word):
        for letter in word:
            if letter not in suffix:
                suffix[letter] = {}
            suffix = suffix[letter]
        suffix["*"] = word
        
    def isSuffix(self, suffix, word):
        for letter in word:
            if letter not in suffix:
                return False
            suffix = suffix[letter]
        return len(suffix) > 1
        