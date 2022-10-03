class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        letters = Counter(chars)
        
        def isGood(word, letters):
            counter = Counter(word)
            for c in counter:
                if letters[c] < counter[c]:
                    return False
            return True
        
        length = 0
        for word in words:
            if isGood(word,letters):
                length += len(word)
        
        return length