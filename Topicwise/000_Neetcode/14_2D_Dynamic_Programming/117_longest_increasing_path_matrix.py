"""
Problem: Longest Increasing Path in a Matrix
Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Description:
    Given an m x n integers matrix, return the length of the longest
    increasing path. From each cell, move in 4 directions (no diagonals,
    no wrapping). A path must be strictly increasing.

Examples:
    Input:  matrix = [[9,9,4],[6,6,8],[2,1,1]]      Output: 4  (1->2->6->9)
    Input:  matrix = [[3,4,5],[3,2,6],[2,2,1]]      Output: 4  (3->4->5->6)

Constraints:
    m == matrix.length, n == matrix[0].length
    1 <= m, n <= 200
    0 <= matrix[i][j] <= 2^31 - 1
"""

from typing import List
from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        @lru_cache(maxsize=None)
        def dfs(r, c):
            best = 1
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            return best

        return max(dfs(r, c) for r in range(rows) for c in range(cols))
