"""
Problem: Surrounded Regions
Link: https://leetcode.com/problems/surrounded-regions/

Description:
    Given an m x n board of 'X' and 'O', capture all 'O' regions surrounded
    by 'X'. A region is surrounded if it is not connected to the border.

Examples:
    Input:  board = [["X","X","X","X"],
                     ["X","O","O","X"],
                     ["X","X","O","X"],
                     ["X","O","X","X"]]
    Output: [["X","X","X","X"],
             ["X","X","X","X"],
             ["X","X","X","X"],
             ["X","O","X","X"]]

Constraints:
    m == board.length, n == board[i].length
    1 <= m, n <= 200
    board[i][j] is 'X' or 'O'
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'S'  # mark as safe (border-connected)
            dfs(r + 1, c); dfs(r - 1, c); dfs(r, c + 1); dfs(r, c - 1)

        # mark all 'O's reachable from the border as safe
        for r in range(rows):
            dfs(r, 0); dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c); dfs(rows - 1, c)

        # flip: safe -> 'O', surrounded -> 'X'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
