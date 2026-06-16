"""
Problem: Counting Bits
Link: https://leetcode.com/problems/counting-bits/

Description:
    Given n, return an array ans where ans[i] is the number of 1 bits
    in the binary representation of i, for 0 <= i <= n.

Examples:
    Input:  n = 2    Output: [0,1,1]
    Input:  n = 5    Output: [0,1,1,2,1,2]

Constraints:
    0 <= n <= 10^5
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # i >> 1 is i//2; its bit count is already known; add the lowest bit of i
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
