"""
Problem: Number of 1 Bits
Link: https://leetcode.com/problems/number-of-1-bits/

Description:
    Given an unsigned integer, return the number of '1' bits (Hamming weight).

Examples:
    Input:  n = 00000000000000000000000000001011    Output: 3
    Input:  n = 00000000000000000000000010000000    Output: 1

Constraints:
    1 <= n <= 2^31 - 1
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1  # clears the lowest set bit each iteration — faster than checking each bit
            count += 1
        return count
