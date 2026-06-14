"""
Problem: Longest Palindromic Substring
Link: https://leetcode.com/problems/longest-palindromic-substring/

Description:
    Given a string s, return the longest palindromic substring.

Examples:
    Input:  s = "babad"    Output: "bab" or "aba"
    Input:  s = "cbbd"     Output: "bb"

Constraints:
    1 <= s.length <= 1000
    s consists of digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""

        def expand(l, r):
            nonlocal best
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(best):
                    best = s[l:r+1]
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)      # odd-length palindromes
            expand(i, i + 1)  # even-length palindromes

        return best
