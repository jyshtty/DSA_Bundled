# leetcode 79: Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
# https://leetcode.com/problems/word-search/
# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Approach: Backtracking
# Time Complexity: O(m*n*4^L) where L is word length
# Space Complexity: O(L)
# Implementation:


class Solution:
    def exist(self, board, word):
        row = len(board)
        col = len(board[0])
        visited = set()

        def bracktrack(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                    r > row - 1 or c > col - 1 or
                    board[r][c] != word[i] or
                    (r, c) in visited):
                return False

            visited.add((r, c))
            res = (bracktrack(r + 1, c, i + 1) or
                   bracktrack(r - 1, c, i + 1) or
                   bracktrack(r, c + 1, i + 1) or
                   bracktrack(r, c - 1, i + 1))
            visited.remove((r, c))
            return res

        for r in range(row):
            for c in range(col):
                if bracktrack(r, c, 0):
                    return True
        return False

