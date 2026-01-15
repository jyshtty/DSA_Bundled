# Rat in a Maze
# Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination.
# The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
# Note: In a path, no cell can be visited more than one time.
# Example:
# Input: N = 4, m[][] = {{1, 0, 0, 0}, {1, 1, 0, 1}, {1, 1, 0, 0}, {0, 1, 1, 1}}
# Output: DDRDRR DRDDRR
# Approach: Backtracking
# Time Complexity: O(4^(n^2))
# Space Complexity: O(n^2)
# Implementation:


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        mat = [[0 for i in range(n)] for j in range(n)]

        def backtrack(mat, i, j):
            if i == n - 1 and j == n - 1:
                mat[n - 1][n - 1] = 1
                return True

            if A[i][j] == 1:
                mat[i][j] = 1
                if i + 1 < n:
                    if backtrack(mat, i + 1, j):
                        return True

                if j + 1 < n:
                    if backtrack(mat, i, j + 1):
                        return True
                mat[i][j] = 0

            else:
                return False

        backtrack(mat, 0, 0)
        return mat