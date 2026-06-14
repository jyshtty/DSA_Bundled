"""
Problem: Swim in Rising Water
Link: https://leetcode.com/problems/swim-in-rising-water/

Description:
    Given n x n grid where grid[i][j] is the elevation at (i,j), find the
    minimum time t such that you can travel from (0,0) to (n-1,n-1) where
    at time t all cells with elevation <= t are reachable.

Examples:
    Input:  grid = [[0,2],[1,3]]    Output: 3
    Input:  grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    Output: 16

Constraints:
    n == grid.length == grid[i].length
    1 <= n <= 50
    0 <= grid[i][j] < n^2
    All values unique.
"""

from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        heap = [(grid[0][0], 0, 0)]  # (max_elevation_so_far, r, c)

        while heap:
            t, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == n-1 and c == n-1:
                return t
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    # bottleneck path: track the maximum elevation seen, not the sum
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))

        return -1
