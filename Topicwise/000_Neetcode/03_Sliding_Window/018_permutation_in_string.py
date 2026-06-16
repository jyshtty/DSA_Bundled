"""
Problem: Permutation in String
Link: https://leetcode.com/problems/permutation-in-string/

Description:
    Given two strings s1 and s2, return true if s2 contains a permutation
    of s1 (i.e., one of s1's permutations is a substring of s2).

Examples:
    Input:  s1 = "ab", s2 = "eidbaooo"    Output: True  ("ba" is in s2)
    Input:  s1 = "ab", s2 = "eidboaoo"    Output: False

Constraints:
    1 <= s1.length, s2.length <= 10^4
    s1 and s2 consist of lowercase English letters.
"""

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = Counter(s1)
        window = Counter(s2[:len(s1)])

        # number of characters whose count matches between window and need
        matches = sum(1 for c in need if window[c] == need[c])

        for i in range(len(s1), len(s2)):
            if matches == len(need):
                return True

            # add new right character
            right_char = s2[i]
            if right_char in need:
                if window[right_char] == need[right_char]:
                    matches -= 1  # about to break a match
                window[right_char] += 1
                if window[right_char] == need[right_char]:
                    matches += 1  # restored a match

            # remove old left character
            left_char = s2[i - len(s1)]
            if left_char in need:
                if window[left_char] == need[left_char]:
                    matches -= 1
                window[left_char] -= 1
                if window[left_char] == need[left_char]:
                    matches += 1

        return matches == len(need)
