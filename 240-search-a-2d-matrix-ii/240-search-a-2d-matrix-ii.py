class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        while row < len(matrix) and matrix[row][0] <= target:
            left, right = 0, len(matrix[0]) - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            row += 1
        return False
            
    