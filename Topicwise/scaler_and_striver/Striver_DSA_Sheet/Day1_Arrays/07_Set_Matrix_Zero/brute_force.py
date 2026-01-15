# leetcode 73: Set Matrix Zeroes
# Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
# https://leetcode.com/problems/set-matrix-zeroes/
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Approach: Brute force - mark rows and columns
# Time Complexity: O(m*n*(m+n))
# Space Complexity: O(m+n)
# Implementation:


# Doesnt work if there is -ve elem in matrix

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_len = len(matrix)
        col_len = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for m in range(col_len):
                        if matrix[i][m] != 0:
                            matrix[i][m] = -1

                    for n in range(row_len):
                        if matrix[n][j] != 0:
                            matrix[n][j] = -1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0
        return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]
obj = Solution()
print(obj.setZeroes(matrix))

# Time Complexity: O((N*M)*(N + M)) + O(N*M
