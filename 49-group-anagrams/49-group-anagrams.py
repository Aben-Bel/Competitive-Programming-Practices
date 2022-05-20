class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        value = defaultdict(list)
        for word in strs:
            sign = self.getSignature(word)
            value[sign].append(word)
        
        return value.values()
            
            
    def getSignature(self, word):
        alpha = [0] * 26
        for char in word:
            alpha[ord(char) - ord('a')]+=1
        
        signature = ""
        for i in range(26):
            if alpha[i] > 0:
                signature += chr(i+65) + str(alpha[i])
        return signature
    
        