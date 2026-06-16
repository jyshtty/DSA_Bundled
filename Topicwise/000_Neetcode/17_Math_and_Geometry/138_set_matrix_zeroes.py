"""
Problem: Set Matrix Zeroes
Link: https://leetcode.com/problems/set-matrix-zeroes/

Description:
    Given an m x n integer matrix, if an element is 0, set its entire
    row and column to 0. Do it in-place.

Examples:
    Input:  [[1,1,1],[1,0,1],[1,1,1]]    Output: [[1,0,1],[0,0,0],[1,0,1]]
    Input:  [[0,1,2,0],[3,4,5,2],[1,3,1,5]]    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
    m == matrix.length, n == matrix[i].length
    1 <= m, n <= 200
    -2^31 <= matrix[i][j] <= 2^31 - 1
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        # first pass: record which rows and cols contain a zero
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        # second pass: apply zeroes — two passes avoid misidentifying original zeroes
        for r in range(rows):
            for c in range(cols):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0
