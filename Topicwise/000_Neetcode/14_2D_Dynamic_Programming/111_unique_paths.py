"""
Problem: Unique Paths
Link: https://leetcode.com/problems/unique-paths/

Description:
    A robot starts at the top-left of an m x n grid and must reach the
    bottom-right. It can only move right or down. Return the number of
    unique paths.

Examples:
    Input:  m = 3, n = 7    Output: 28
    Input:  m = 3, n = 2    Output: 3

Constraints:
    1 <= m, n <= 100
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[c] = number of ways to reach the cell in the current row at column c
        dp = [1] * n  # top row always has exactly 1 path (only go right)

        for _ in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c - 1]  # from above (dp[c]) + from the left (dp[c-1])

        return dp[n - 1]
