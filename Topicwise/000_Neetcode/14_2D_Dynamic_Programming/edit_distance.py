"""
Problem: Edit Distance
Link: https://leetcode.com/problems/edit-distance/

Description:
    Given two strings word1 and word2, return the minimum operations
    (insert, delete, replace) to convert word1 to word2.

Examples:
    Input:  word1 = "horse", word2 = "ros"    Output: 3
    Input:  word1 = "intention", word2 = "execution"    Output: 5

Constraints:
    0 <= word1.length, word2.length <= 500
    word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # dp[i][j] = edit distance between word1[:i] and word2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i  # delete all chars of word1
        for j in range(n + 1):
            dp[0][j] = j  # insert all chars of word2

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]  # chars match — no operation needed
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],    # delete from word1
                        dp[i][j-1],    # insert into word1
                        dp[i-1][j-1]   # replace
                    )

        return dp[m][n]
