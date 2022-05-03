class Solution:
    def __init__(self):
        self.longest = ""
        
    def longestWord(self, words: List[str]) -> str:
        trie = [None]*27
        
        for word in words:
            self.addWord(trie, word)
        
        self.searchLongest(trie)
        return self.longest
    
    def addWord(self, node, word):
        for letter in word:
            charVal = ord(letter) - ord('a')
            if node[charVal] == None:
                node[charVal] = [None]*27
            node = node[charVal]
        node[26] = word
        
    def searchLongest(self, node):
        
        for i in range(26):
            if node[i]!=None:
                if node[i][26] != None:
                    if len(self.longest) < len(node[i][26]):
                        self.longest = node[i][26]
                    self.searchLongest(node[i])
    