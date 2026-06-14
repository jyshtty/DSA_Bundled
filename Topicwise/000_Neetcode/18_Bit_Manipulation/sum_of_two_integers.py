"""
Problem: Sum of Two Integers
Link: https://leetcode.com/problems/sum-of-two-integers/

Description:
    Given two integers a and b, return their sum without using + or -.

Examples:
    Input:  a = 1, b = 2    Output: 3
    Input:  a = 2, b = 3    Output: 5

Constraints:
    -1000 <= a, b <= 1000
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # 32-bit mask to simulate overflow behavior

        while b & mask:
            carry = (a & b) << 1   # carry bits
            a = a ^ b              # sum without carry
            b = carry

        # if b is non-zero after the loop, it's a negative number that needs sign extension
        return a if b == 0 else a & mask
