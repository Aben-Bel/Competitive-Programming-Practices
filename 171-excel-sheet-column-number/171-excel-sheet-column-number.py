class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = 0
        result = 0
        for char in reversed(columnTitle):
            val = ord(char) - ord("A") + 1
            result += val*(26**base)
            base+=1
        return result