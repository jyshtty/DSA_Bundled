"""
Problem: Minimum Window Substring
Link: https://leetcode.com/problems/minimum-window-substring/

Description:
    Given strings s and t, return the minimum window substring of s that
    contains every character in t (including duplicates). If no such
    substring exists, return "".

Examples:
    Input:  s = "ADOBECODEBANC", t = "ABC"    Output: "BANC"
    Input:  s = "a", t = "a"                  Output: "a"
    Input:  s = "a", t = "aa"                 Output: ""

Constraints:
    1 <= s.length, t.length <= 10^5
    s and t consist of uppercase and lowercase English letters.
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)  # total characters still needed in the window
        left = 0
        best_left, best_right = 0, float('inf')

        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1  # only decrement when we actually needed this char
            need[ch] -= 1

            if missing == 0:  # window contains all required characters
                # shrink from left while window remains valid
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if right - left < best_right - best_left:
                    best_left, best_right = left, right

                # move left past the matched char to search for a smaller window
                need[s[left]] += 1
                missing += 1
                left += 1

        return "" if best_right == float('inf') else s[best_left: best_right + 1]
