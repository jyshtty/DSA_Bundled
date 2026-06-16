"""
Problem: Number of Islands
Link: https://leetcode.com/problems/number-of-islands/

Description:
    Given an m x n 2D binary grid of '1' (land) and '0' (water),
    return the number of islands. An island is surrounded by water and
    formed by connecting adjacent land cells horizontally or vertically.

Examples:
    Input:  grid = [["1","1","1","1","0"],
                    ["1","1","0","1","0"],
                    ["1","1","0","0","0"],
                    ["0","0","0","0","0"]]    Output: 1

    Input:  grid = [["1","1","0","0","0"],
                    ["1","1","0","0","0"],
                    ["0","0","1","0","0"],
                    ["0","0","0","1","1"]]    Output: 3

Constraints:
    m == grid.length, n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != '1':
                return
            grid[r][c] = '0'  # mark visited by sinking the land cell
            dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1

        return count
