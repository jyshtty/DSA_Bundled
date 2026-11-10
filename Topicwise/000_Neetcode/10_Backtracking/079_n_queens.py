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

class Solution:
    def solveNQueens(self, n):
        matrix = [["." for i in range(n)] for j in range(n)]
        col = [False] * n
        # diagonal (↙↗ or ↘↖) in an n × n chessboard represents a unique line across the board.
        # There are a total of 2n - 1 such diagonals in each direction.
        left_diag = [False] * (2 * n - 1)
        right_diag = [False] * (2 * n - 1)
        ans = []

        def backtrack(r, matrix, col, left_diag, right_diag):
            if r == n:
                temp = ["".join(x) for x in matrix]
                ans.append(temp)
                return 
                
            for column in range(n):
                if col[column] == False and left_diag[r - column + n - 1] == False and right_diag[r + column] == False:
                    # safe to place queen
                    matrix[r][column] = 'Q'

                    col[column] = True
                    left_diag[r - column + n - 1] = True
                    right_diag[r + column] = True

                    backtrack(r + 1, matrix, col, left_diag, right_diag)

                    matrix[r][column] = '.'

                    col[column] = False
                    left_diag[r - column + n - 1] = False
                    right_diag[r + column] = False

        backtrack(0, matrix, col, left_diag, right_diag)
        return ans
