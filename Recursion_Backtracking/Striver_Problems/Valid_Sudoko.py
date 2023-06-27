# Not Backtracking.
# Very simple - Check Neetcode explanation.
# Understand the question. They are just asking if any of already filled number is contradicting.

# Keep 3 hash maps where value is a set - cols, rows, squares
# if you divide row//3 and col//3 and keep tuple of result as key to the squares hashamp,
# ex - if row,col is 5,5 - squares[(2,2)] = set(1,2,3)


import collections

class Solution:
    def isValidSudoku(self, board):
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
