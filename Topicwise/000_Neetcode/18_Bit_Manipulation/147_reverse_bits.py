"""
Problem: Reverse Bits
Link: https://leetcode.com/problems/reverse-bits/

Description:
    Reverse the bits of a given 32-bit unsigned integer.

Examples:
    Input:  n = 00000010100101000001111010011100    Output: 964176192
    Input:  n = 11111111111111111111111111111101    Output: 3221225471

Constraints:
    The input must be a binary string of length 32.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)  # shift result left, append LSB of n
            n >>= 1
        return result
