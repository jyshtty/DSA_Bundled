"""
Problem: Search a 2D Matrix
Link: https://leetcode.com/problems/search-a-2d-matrix/

Description:
    Given an m x n integer matrix where each row is sorted and the first
    integer of each row is greater than the last of the previous row,
    return true if target exists in the matrix.

Examples:
    Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: True

    Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: False

Constraints:
    m == matrix.length, n == matrix[i].length
    1 <= m, n <= 100
    -10^4 <= matrix[i][j], target <= 10^4
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            # treat the 2D matrix as a flattened sorted array
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
