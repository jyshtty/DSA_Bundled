"""
Problem: N-Queens
Link: https://leetcode.com/problems/n-queens/

Description:
    Place n queens on an n×n chessboard so that no two queens attack each other.
    Return all distinct solutions where 'Q' is a queen and '.' is empty.

Examples:
    Input:  n = 4
    Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

    Input:  n = 1    Output: [["Q"]]

Constraints:
    1 <= n <= 9
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set()   # top-left to bottom-right: row - col is constant on same diagonal
        diag2 = set()   # top-right to bottom-left: row + col is constant on same diagonal
        board = [['.' ] * n for _ in range(n)]
        result = []

        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board[row][col] = 'Q'
                backtrack(row + 1)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                board[row][col] = '.'

        backtrack(0)
        return result
