class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = [[],[],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
        result = []
        self.build(mapping, digits, 0, "", result)
        return result
    
    def build(self, mapping, digits, i, current, result):
        if len(digits) == len(current):
            if current: result.append(current)
            return
            
        for digit in mapping[int(digits[i])]:
            self.build(mapping, digits, i+1, current + digit, result)