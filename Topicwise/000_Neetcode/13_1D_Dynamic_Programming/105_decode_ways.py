"""
Problem: Decode Ways
Link: https://leetcode.com/problems/decode-ways/

Description:
    A message encoded as digits where A=1, B=2, ..., Z=26.
    Given a string s of digits, return the number of ways to decode it.

Examples:
    Input:  s = "12"    Output: 2    ('AB' or 'L')
    Input:  s = "226"   Output: 3    ('BZ', 'VF', 'BBF')
    Input:  s = "06"    Output: 0

Constraints:
    1 <= s.length <= 100
    s contains only digits
    s may contain leading zeros
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i] = number of ways to decode s[:i]
        dp = [0] * (n + 1)
        dp[0] = 1  # empty string has one decoding
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, n + 1):
            one = int(s[i-1])        # single digit
            two = int(s[i-2:i])      # two digits

            if one != 0:             # '0' can't stand alone
                dp[i] += dp[i-1]
            if 10 <= two <= 26:      # two-digit codes are only 10-26
                dp[i] += dp[i-2]

        return dp[n]
