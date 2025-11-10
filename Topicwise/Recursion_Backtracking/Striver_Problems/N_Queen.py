# N-Queens Problem
# Problem Statement: Place N queens on an N x N chessboard such that no two queens threaten each other.
# A queen can attack another queen if they are in the same row, column, or diagonal.
# The solution should return all distinct configurations of the board where the queens are placed safely.

# Example usage:
# sol = Solution()
# print(sol.solveNQueens(4))    

# input: 4
# output: [
#  [".Q..",
#   "...Q",
#   "Q...",
#   "..Q."],
#  ["..Q.",
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Each solution contains a distinct board configuration of the N-Queens' placement.
# The '.' character indicates an empty square, and 'Q' indicates a queen.
# The solution should return all distinct configurations of the board where the queens are placed safely.
# No two queens should threaten each other.
# The order of the solutions does not matter.
# You may return the answer in any order.
# Constraints:
# 1 <= n <= 9
# Follow up: Could you solve the problem using bit manipulation to optimize the space complexity?


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
