"""
Problem: Max Area of Island
Link: https://leetcode.com/problems/max-area-of-island/

Description:
    Given a binary matrix grid (0=water, 1=land), return the maximum area
    of an island. An island is a group of 1s connected 4-directionally.

Examples:
    Input:  [[0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0]]    Output: 6

Constraints:
    m == grid.length, n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is 0 or 1.
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0  # sink to avoid revisiting
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        return max(dfs(r, c) for r in range(rows) for c in range(cols))
