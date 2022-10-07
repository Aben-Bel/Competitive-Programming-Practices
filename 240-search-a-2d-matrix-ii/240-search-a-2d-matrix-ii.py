class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1
        while True:
            if row < len(matrix) - 1 and target > matrix[row][col]:
                row += 1
            elif col > -1 and target < matrix[row][col]:
                col -= 1
            elif matrix[row][col] == target:
                return True
            else:
                return False
        return False
    