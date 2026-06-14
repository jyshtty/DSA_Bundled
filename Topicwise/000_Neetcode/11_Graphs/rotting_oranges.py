"""
Problem: Rotting Oranges
Link: https://leetcode.com/problems/rotting-oranges/

Description:
    Each minute, any fresh orange 4-directionally adjacent to a rotten one
    becomes rotten. Return the minimum minutes until no fresh orange remains,
    or -1 if impossible.

Examples:
    Input:  [[2,1,1],[1,1,0],[0,1,1]]    Output: 4
    Input:  [[2,1,1],[0,1,1],[1,0,1]]    Output: -1
    Input:  [[0,2]]                       Output: 0

Constraints:
    m == grid.length, n == grid[i].length
    1 <= m, n <= 10
    grid[i][j] is 0, 1, or 2.
"""

from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # seed BFS with all initially rotten oranges
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while queue:
            r, c, t = queue.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    minutes = t + 1
                    queue.append((nr, nc, t + 1))

        return minutes if fresh == 0 else -1
