class Solution:
    def __init__(self):
        self.count = 0
        
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = [None]*27
        for word in words:
            self.addWord(trie, word)
        
        result = []
        self.getWords(s, trie, 0)
        return self.count
    
    def addWord(self, trie, word):
        node = trie
        for letter in word:
            charVal = ord(letter) - ord('a')
            if node[charVal] == None:
                node[charVal] = [None]*27
            node = node[charVal]
        if node[26] != None: 
            node[26]+=1
        else: 
            node[26] = 1
        
    def check(self, s, i, char):
        for j in range(i, len(s)):
            if s[j] == char:
                return j
            
        return -1
    
    def getWords(self, s, trie, k):
        node = trie
        for i in range(26):
            if node[i] != None:
                exists = self.check(s, k, chr(i+ord('a')))
                if exists != -1:
                    self.getWords(s, node[i], exists+1)
                    if node[i][26] != None:
                        self.count += node[i][26]
                        # print(node[i][26])
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    