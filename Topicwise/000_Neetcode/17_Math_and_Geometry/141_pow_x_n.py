"""
Problem: Pow(x, n)
Link: https://leetcode.com/problems/powx-n/

Description:
    Implement pow(x, n), which calculates x raised to the power n.

Examples:
    Input:  x = 2.0, n = 10     Output: 1024.0
    Input:  x = 2.1, n = 3      Output: 9.261
    Input:  x = 2.0, n = -2     Output: 0.25

Constraints:
    -100.0 < x < 100.0
    -2^31 <= n <= 2^31 - 1
    -10^4 <= x^n <= 10^4
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        while n:
            if n % 2 == 1:
                result *= x
            x *= x      # square the base each iteration
            n //= 2     # fast exponentiation: O(log n) multiplications

        return result
