class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        elements = set()
        countZeros = 0
        for num in arr:
            if num == 0:
                countZeros += 1
            elements.add(num)
        
        for num in arr:
            if num == 0 and countZeros <= 1:
                continue
            
            if num*2 in elements:
                return True
        
        return False