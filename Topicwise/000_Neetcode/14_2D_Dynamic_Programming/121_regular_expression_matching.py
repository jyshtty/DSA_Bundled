"""
Problem: Regular Expression Matching
Link: https://leetcode.com/problems/regular-expression-matching/

Description:
    Given string s and pattern p, implement regex matching where:
    '.' matches any single character.
    '*' matches zero or more of the preceding element.

Examples:
    Input:  s = "aa", p = "a*"     Output: True
    Input:  s = "ab", p = ".*"     Output: True
    Input:  s = "aab", p = "c*a*b" Output: True

Constraints:
    1 <= s.length <= 20
    1 <= p.length <= 30
    s contains only lowercase letters.
    p contains lowercase letters, '.', and '*'.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # empty string matches empty pattern

        # patterns like a*, a*b*, a*b*c* can match an empty string
        for j in range(2, n + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == '*':
                    # zero occurrences of preceding element
                    dp[i][j] = dp[i][j-2]
                    # one or more occurrences: preceding element must match current char
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                elif p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[m][n]
