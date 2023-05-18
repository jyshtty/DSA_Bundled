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