class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        trie = {}
        
        self.addWord(trie, pattern)
        output = [False for i in range(len(queries))]
        for i, query in enumerate(queries):
            output[i] = self.search(trie, query)
        return output
    
    def addWord(self, node, pattern):
        camelCase = ""
        for letter in pattern:
            if letter.isupper():
                camelCase+=letter
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node["*"] = (pattern, camelCase)
    
    def search(self, node, query):
        camelCase = ""
        for letter in query:
            if letter.isupper():
                camelCase+=letter
                
        for letter in query:
            if letter in node:
                node = node[letter]
            
        if "*" in node and node["*"][1] == camelCase:
            return True
        return False