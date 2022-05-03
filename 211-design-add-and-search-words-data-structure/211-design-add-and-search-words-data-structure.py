class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['*'] = True

    def search(self, word: str) -> bool:
        return self.searchWithDot(self.trie, word)
    
    def searchWithDot(self, node, word):
        for i in range(len(word)):
            letter = word[i]
            if letter not in node:
                if letter == ".":
                    exist = False
                    for key in node:
                        if key != "*":
                            exist = exist or self.searchWithDot(node[key], word[i+1:])
                            if exist:
                                return True
                return False
            else:
                node = node[letter]
        return "*" in node
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)