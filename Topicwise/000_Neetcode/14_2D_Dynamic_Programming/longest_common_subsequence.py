"""
Problem: Longest Common Subsequence
Link: https://leetcode.com/problems/longest-common-subsequence/

Description:
    Given two strings text1 and text2, return the length of their longest
    common subsequence. Return 0 if none.

Examples:
    Input:  text1 = "abcde", text2 = "ace"    Output: 3  ("ace")
    Input:  text1 = "abc", text2 = "abc"      Output: 3
    Input:  text1 = "abc", text2 = "def"      Output: 0

Constraints:
    1 <= text1.length, text2.length <= 1000
    text1 and text2 consist of only lowercase English characters.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # only keep two rows to reduce space from O(mn) to O(n)
        prev = [0] * (n + 1)

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr

        return prev[n]
