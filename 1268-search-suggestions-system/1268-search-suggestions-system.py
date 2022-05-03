class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = [None]*27
        for product in products:
            self.addWord(product, trie)
        
        result = []
        for i in range(len(searchWord)):
            w = self.search(searchWord[:i+1], trie)
            result.append(w[:min(3,len(w))])
        return result
            
    
    def addWord(self, product, trie):
        node = trie
        for letter in product:
            charVal = ord(letter) - ord('a')
            if node[charVal] == None:
                node[charVal] = [None]*27
            node = node[charVal]
        node[26] = product
        
    def search(self, word, trie):
        count = 0
        node = trie
        c = ord(word[0]) - ord('a')
        if node[c] == None: 
            return []
        
        for letter in word:
            charVal = ord(letter) - ord('a')
            if node[charVal] == None:
                return []
            
            node = node[charVal]
            
        result = []
        self.collectWords(node, result)
        return result
    
    def collectWords(self, node, result):
        if len(result) == 3:
            return
        
        if node[26] != None:
            result.append(node[26])
        
        
        for i in range(26):
            if node[i] != None:
                self.collectWords(node[i], result)
        
    
    