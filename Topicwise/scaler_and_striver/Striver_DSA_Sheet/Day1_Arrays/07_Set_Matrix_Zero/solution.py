# leetcode 73: Set Matrix Zeroes
# Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
# https://leetcode.com/problems/set-matrix-zeroes/
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Approach: Use first row and column as markers
# Time Complexity: O(m*n)
# Space Complexity: O(1)
# Implementation:


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_array = len(matrix) * [0]
        col_array = len(matrix[0]) * [0]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_array[i] = 1
                    col_array[j] = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row_array[i] == 1 or col_array[j] == 1:
                    matrix[i][j] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
obj = Solution()
print(obj.setZeroes(matrix))