"""
Problem: Pacific Atlantic Water Flow
Link: https://leetcode.com/problems/pacific-atlantic-water-flow/

Description:
    Given an m x n island, water flows to Pacific (top/left edges) or
    Atlantic (bottom/right edges) if it can flow to a neighbor with equal
    or lesser height. Return cells that can flow to both oceans.

Examples:
    Input:  heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Constraints:
    m == heights.length, n == heights[i].length
    1 <= m, n <= 200
    0 <= heights[i][j] <= 10^5
"""

from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr, nc = r + dr, c + dc
                    # flow in reverse: move to higher/equal cells from the ocean border
                    if (0 <= nr < rows and 0 <= nc < cols and
                            (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        pacific_starts  = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atlantic_starts = [(r, cols-1) for r in range(rows)] + [(rows-1, c) for c in range(cols)]

        pac = bfs(pacific_starts)
        atl = bfs(atlantic_starts)

        return [[r, c] for r, c in pac & atl]
