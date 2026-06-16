"""
Problem: Distinct Subsequences
Link: https://leetcode.com/problems/distinct-subsequences/

Description:
    Given strings s and t, return the number of distinct subsequences of s
    which equals t.

Examples:
    Input:  s = "rabbbit", t = "rabbit"    Output: 3
    Input:  s = "babgbag", t = "bag"       Output: 5

Constraints:
    1 <= s.length, t.length <= 1000
    s and t consist of English letters.
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # dp[j] = number of ways to form t[:j] using s seen so far
        dp = [0] * (n + 1)
        dp[0] = 1  # empty t is always a subsequence

        for ch_s in s:
            # iterate backwards so we don't use the same s character twice
            for j in range(n, 0, -1):
                if ch_s == t[j-1]:
                    dp[j] += dp[j-1]

        return dp[n]
