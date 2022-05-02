class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = {}
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else: 
                frequency[word] = 0
        
        bucket = [[None]*27 for i in range(len(words))]
        usedFreq = set()
        for key in frequency:
            word = key
            freq = frequency[key]
            self.addWord(bucket[freq], word)
            usedFreq.add(freq)
        
        ans = []
        for i in range(len(words), -1, -1):
            if i in usedFreq:
                result = []
                self.getWords(bucket[i], result)
                if i==9:
                    print(result)
                if len(result) < k:
                    ans.extend(result)
                    k = k - len(result)
                else:
                    ans.extend(result[0:k])
                    break
        return ans
            
            
    def addWord(self, trie, word):
        node = trie
        for char in word:
            charVal = ord(char)-ord('a')
            if node[charVal] == None:
                node[charVal] = [None]*27
            node = node[charVal]
        node[26] = word
    
    def getWords(self, trie, result):
        if trie[26] != None:
            result.append(trie[26])
        
        node = trie
        for i in range(26):
            if node[i] != None:
                self.getWords(node[i], result)
        
            