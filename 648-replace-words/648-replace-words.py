class Solution: 
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = [None]*27
        
        def insert(word, trie):
            for c in word:
                idx = ord(c)-ord('a')
                if trie[idx] == None:
                    trie[idx] = [None]*27
                trie = trie[idx]
            trie[-1] = word
        
        def hasPrefix(word, trie):
            for c in word:
                idx = ord(c) - ord('a')
                if trie[idx] == None or trie[-1] != None:
                    return trie[-1]
                trie = trie[idx]
            return trie[-1]
                
                
        for word in dictionary:
            insert(word, trie)
        sentence = sentence.split(" ")
        for i in range(len(sentence)):
            val = hasPrefix(sentence[i],trie)
            if val != None:
                sentence[i] = val
        return " ".join(sentence)
            
                