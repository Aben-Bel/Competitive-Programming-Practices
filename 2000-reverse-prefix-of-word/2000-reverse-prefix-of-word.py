class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = 0
        for char in word:
            if ch == char:
                break
            i+=1
        
        if i<len(word):
            return word[:i+1][::-1] + word[i+1:]
        else:
            return word