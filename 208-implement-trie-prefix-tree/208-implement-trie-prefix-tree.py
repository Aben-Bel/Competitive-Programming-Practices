class Trie:

    def __init__(self):
        self.nodes = [None]*26
        self.end = False
        self.value = None
        
    def insert(self, word: str) -> None:
        node = self
        for i in range(len(word)):
            cur = word[i]
            l = ord(cur)-ord('a')
            if not node.nodes[l]:
                node.nodes[l] = Trie()
                node.nodes[l].value = cur
            
            if i == len(word)-1:
                node.nodes[l].end = True
                break
            
            node = node.nodes[l]

    def search(self, word: str) -> bool:
        node = self
        for i in range(len(word)):
            cur = word[i]
            l = ord(cur)-ord('a')
            if not node.nodes[l]:
                return False
            
            if i == len(word)-1 and node.nodes[l].end == False:
                return False
            
            node = node.nodes[l]
        
        return True

    def startsWith(self, prefix: str) -> bool:
        node = self
        for i in range(len(prefix)):
            cur = prefix[i]
            l = ord(cur)-ord('a')
            if not node.nodes[l]:
                return False
            node = node.nodes[l]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)