"""
Problem: Interleaving String
Link: https://leetcode.com/problems/interleaving-string/

Description:
    Given strings s1, s2, s3, return true if s3 is formed by interleaving s1 and s2.
    Interleaving preserves the relative order of characters from each string.

Examples:
    Input:  s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"   Output: True
    Input:  s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"   Output: False

Constraints:
    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1, s2, s3 consist of lowercase English letters.
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        # dp[i][j] = can s3[:i+j] be formed by s1[:i] and s2[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                k = i + j - 1  # index into s3
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[k]) or \
                            (dp[i][j-1] and s2[j-1] == s3[k])

        return dp[m][n]
