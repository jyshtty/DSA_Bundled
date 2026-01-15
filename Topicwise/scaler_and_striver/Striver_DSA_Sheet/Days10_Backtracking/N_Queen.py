# leetcode 51: N-Queens
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' indicate a queen and an empty space, respectively.
# https://leetcode.com/problems/n-queens/
# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Approach: Backtracking
# Time Complexity: O(n!)
# Space Complexity: O(n^2)
# Implementation:


class Solution:
    def solveNQueens(self, n):
        matrix = [["." for i in range(n)] for j in range(n)]
        col = [False] * n
        left_diag = [False] * (2 * n - 1)
        right_diag = [False] * (2 * n - 1)
        ans = []

        def backtrack(r, matrix, col, left_diag, right_diag):
            if r == n:
                temp = ["".join(x) for x in matrix]

                ans.append(temp)
            for column in range(n):
                if col[column] == False and left_diag[r - column + n - 1] == False and right_diag[r + column] == False:
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