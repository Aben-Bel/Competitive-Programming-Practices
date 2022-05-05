class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        suffix = {}
        num_hashs = 0
        countMergedWords = 0
        words = sorted(words, key= lambda x:len(x))
        print(words)
        for j in range(len(words)-1,-1,-1):
            word = words[j]
            if self.search(suffix, word):
                countMergedWords += len(word)
                continue 
                
            num_hashs += 1
            for i in range(len(word)):
                self.addWord(suffix, i, word)
        
        return num_hashs + sum(map(len,words)) - countMergedWords
        
    def addWord(self, suffix, i, w):
        word = w[i:]
        for letter in word:
            if letter not in suffix:
                suffix[letter] = {}
            suffix = suffix[letter]
        suffix["*"] = word
        
    def search(self, suffix, word):
        for letter in word:
            if letter not in suffix:
                return False
            suffix = suffix[letter]
        return "*" in suffix
            
        