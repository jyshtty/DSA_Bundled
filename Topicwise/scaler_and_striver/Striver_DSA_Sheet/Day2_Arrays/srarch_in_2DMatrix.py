# leetcode 74: Search a 2D Matrix
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# https://leetcode.com/problems/search-a-2d-matrix/
# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Approach: Binary search
# Time Complexity: O(log(m*n))
# Space Complexity: O(1)
# Implementation:


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
