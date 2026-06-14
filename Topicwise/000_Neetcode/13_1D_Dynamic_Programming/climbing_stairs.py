"""
Problem: Climbing Stairs
Link: https://leetcode.com/problems/climbing-stairs/

Description:
    You can climb 1 or 2 steps at a time. Given n steps, return the number
    of distinct ways to reach the top.

Examples:
    Input:  n = 2    Output: 2  (1+1, 2)
    Input:  n = 3    Output: 3  (1+1+1, 1+2, 2+1)

Constraints:
    1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # ways(n) = ways(n-1) + ways(n-2) — same recurrence as Fibonacci
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
