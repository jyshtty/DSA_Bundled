# leetcode 37: Sudoku Solver
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
# https://leetcode.com/problems/sudoku-solver/
# Example 1:
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Approach: Backtracking
# Time Complexity: O(9^(81-k)) where k is number of filled cells
# Space Complexity: O(1)
# Implementation:


# https://leetcode.com/problems/sudoku-solver/
class Solution:
    def solveSudoku(self, board):
        board = []

        def check(board, row, col, k):
            k = str(k)
            for i in range(9):
                if board[i][col] == k or board[row][i] == k:
                    return False
            new_r = row - row % 3
            new_c = col - col % 3

            for i in range(new_r, new_r + 3):
                for j in range(new_c, new_c + 3):
                    if board[i][j] == k:
                        return False
            return True

        def bracktrack(i):
            if i == 81:
                return True

            row = i // 9
            col = i % 9

            if board[row][col] != ".":
                return bracktrack(i + 1)

            for k in range(1, 10):
                if check(board, row, col, k):
                    board[row][col] = str(k)
                    if bracktrack(i + 1):
                        return True
                    board[row][col] = "."
            return False

        bracktrack(0)
        return board

if __name__ == "__main__":
    A =[["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
    obj = Solution()
    print(obj.solveSudoku(A))