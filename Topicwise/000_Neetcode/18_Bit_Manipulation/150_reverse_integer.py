"""
Problem: Reverse Integer
Link: https://leetcode.com/problems/reverse-integer/

Description:
    Given a 32-bit signed integer x, return x with its digits reversed.
    If reversing causes overflow outside [-2^31, 2^31 - 1], return 0.

Examples:
    Input:  x = 123     Output: 321
    Input:  x = -123    Output: -321
    Input:  x = 120     Output: 21

Constraints:
    -2^31 <= x <= 2^31 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = int(str(x)[::-1])
        result = sign * rev

        # return 0 on overflow instead of wrapping (unlike C/Java, Python ints don't overflow)
        return result if INT_MIN <= result <= INT_MAX else 0
