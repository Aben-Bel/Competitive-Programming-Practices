class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []
        
        for char in s:
            if char == "#" and stackS:
                stackS.pop()
            elif char != "#":
                stackS.append(char)
        
        for char in t:
            if char == "#" and stackT:
                stackT.pop()
            elif char != "#":
                stackT.append(char)
        return stackS == stackT