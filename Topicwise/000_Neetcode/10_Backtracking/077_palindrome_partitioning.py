"""
Problem: Palindrome Partitioning
Link: https://leetcode.com/problems/palindrome-partitioning/

Description:
    Given a string s, partition s such that every substring is a palindrome.
    Return all possible palindrome partitioning of s.

Examples:
    Input:  s = "aab"    Output: [["a","a","b"],["aa","b"]]
    Input:  s = "a"      Output: [["a"]]

Constraints:
    1 <= s.length <= 16
    s consists of lowercase English letters.
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, current):
            if start == len(s):
                result.append(current[:])
                return
            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if is_palindrome(substr):
                    current.append(substr)
                    backtrack(end, current)
                    current.pop()

        backtrack(0, [])
        return result
