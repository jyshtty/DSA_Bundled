"""
Problem: Walls and Gates
Link: https://leetcode.com/problems/walls-and-gates/

Description:
    You are given a m x n 2D grid initialized with three values:
    -1 (wall), 0 (gate), INF (empty room = 2147483647).
    Fill each empty room with the distance to its nearest gate.
    If impossible to reach a gate, leave it as INF.

Examples:
    Input:  [[INF,-1,0,INF],
             [INF,INF,INF,-1],
             [INF,-1,INF,-1],
             [0,-1,INF,INF]]
    Output: [[3,-1,0,1],
             [2,2,1,-1],
             [1,-1,2,-1],
             [0,-1,3,4]]

Constraints:
    m == rooms.length, n == rooms[0].length
    1 <= m, n <= 250
    rooms[i][j] is -1, 0, or 2^31 - 1
"""

from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(rooms), len(rooms[0])
        queue = deque()

        # seed BFS from all gates simultaneously — multi-source BFS guarantees shortest distance
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                        rooms[nr][nc] = rooms[r][c] + 1
                        queue.append((nr, nc))
