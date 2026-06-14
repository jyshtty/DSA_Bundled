"""
Problem: Word Search
Link: https://leetcode.com/problems/word-search/

Description:
    Given an m x n grid of characters and a string word, return true if
    the word exists in the grid. The word can be formed by sequentially
    adjacent cells (horizontal or vertical). No cell may be reused.

Examples:
    Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
            word = "ABCCED"    Output: True
    Input:  same board, word = "SEE"    Output: True
    Input:  same board, word = "ABCB"   Output: False

Constraints:
    m == board.length, n == board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[idx]:
                return False

            board[r][c] = '#'  # mark as visited in-place — avoids a separate visited set
            found = (dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or
                     dfs(r, c+1, idx+1) or dfs(r, c-1, idx+1))
            board[r][c] = word[idx]  # restore for other paths
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
