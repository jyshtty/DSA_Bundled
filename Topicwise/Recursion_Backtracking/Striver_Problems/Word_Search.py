# Example usage:
# Input: board = [["A","B","C","E"],
#                 ["S","F","C","S"],
#                 ["A","D","E","E"]], word = "ABCCED"
# Output: True

# Input: board = [["A","B","C","E"],
#                 ["S","F","C","S"],
#                 ["A","D","E","E"]], word = "SEE"
# Output: True
# Input: board = [["A","B","C","E"],
#                 ["S","F","C","S"],
#                 ["A","D","E","E"]], word = "ABCB"
# Output: False 

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution:
    def exist(self, board, word):
        row = len(board)
        col = len(board[0])
        visited = set()

        def backtrack(r, c, i):
            if i == len(word): # If we have found the word
                return True
            if (r < 0 or c < 0 or
                    r > row - 1 or c > col - 1 or # Out of bounds
                    board[r][c] != word[i] or # Character does not match
                    (r, c) in visited): # to avoid circle. To avoid same position twice.
                return False

            visited.add((r, c)) # Mark the cell as visited
            res = (backtrack(r + 1, c, i + 1) or # Explore all 4 directions
                   backtrack(r - 1, c, i + 1) or
                   backtrack(r, c + 1, i + 1) or
                   backtrack(r, c - 1, i + 1))
            visited.remove((r, c)) # Unmark the cell for other paths
            return res # Return whether we found the word

        for r in range(row):
            for c in range(col):
                if backtrack(r, c, 0):
                    return True
        return False

