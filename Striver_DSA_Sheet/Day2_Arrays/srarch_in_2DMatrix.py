# Leetcode 74

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l = len(matrix)
        col_l = len(matrix[0])

        i, j = 0, col_l - 1

        while j >= 0 and i < len(matrix):
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False
