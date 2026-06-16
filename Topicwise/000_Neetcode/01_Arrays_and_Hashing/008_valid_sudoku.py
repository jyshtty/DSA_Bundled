"""
Problem: Valid Sudoku
Link: https://leetcode.com/problems/valid-sudoku/

Description:
    Determine if a 9x9 Sudoku board is valid based on the following rules:
    - Each row must contain digits 1-9 with no repetition.
    - Each column must contain digits 1-9 with no repetition.
    - Each of the nine 3x3 sub-boxes must contain digits 1-9 with no repetition.
    Only filled cells need to be validated.

Examples:
    Input: board =
        [["5","3",".",".","7",".",".",".","."]
         ["6",".",".","1","9","5",".",".","."]
         [".","9","8",".",".",".",".","6","."]
         ["8",".",".",".","6",".",".",".","3"]
         ["4",".",".","8",".","3",".",".","1"]
         ["7",".",".",".","2",".",".",".","6"]
         [".","6",".",".",".",".","2","8","."]
         [".",".",".","4","1","9",".",".","5"]
         [".",".",".",".","8",".",".","7","9"]]
    Output: True

Constraints:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'
"""

from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)  # key = (row//3, col//3) identifies the 3x3 box

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                box_key = (r // 3, c // 3)

                # check all three constraints at once before inserting
                if val in rows[r] or val in cols[c] or val in boxes[box_key]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_key].add(val)

        return True
