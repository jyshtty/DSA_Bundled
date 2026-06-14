"""
Problem: Plus One
Link: https://leetcode.com/problems/plus-one/

Description:
    Given a large integer represented as a digit array, increment by one
    and return the resulting array.

Examples:
    Input:  digits = [1,2,3]    Output: [1,2,4]
    Input:  digits = [9]        Output: [1,0]
    Input:  digits = [9,9]      Output: [1,0,0]

Constraints:
    1 <= digits.length <= 100
    0 <= digits[i] <= 9
    digits does not contain leading zeros.
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # carry: 9 + 1 = 10, write 0 and carry 1

        # all digits were 9 (e.g. [9,9] -> [1,0,0])
        return [1] + digits
