"""
Problem: Rotate Image
Link: https://leetcode.com/problems/rotate-image/

Description:
    Given an n x n matrix, rotate it 90 degrees clockwise in-place.

Examples:
    Input:  [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # step 1: transpose — swap across the main diagonal
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # step 2: reverse each row — together with transpose this gives a 90° clockwise rotation
        for row in matrix:
            row.reverse()
