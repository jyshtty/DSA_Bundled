"""
Problem: Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Description:
    Given a string s, find the length of the longest substring without
    repeating characters.

Examples:
    Input:  s = "abcabcbb"    Output: 3  ("abc")
    Input:  s = "bbbbb"       Output: 1  ("b")
    Input:  s = "pwwkew"      Output: 3  ("wke")

Constraints:
    0 <= s.length <= 5 * 10^4
    s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # maps char -> its most recent index in the string
        left = 0
        best = 0

        for right, ch in enumerate(s):
            # if char was seen and is inside the current window, shrink from the left
            if ch in char_index and char_index[ch] >= left:
                left = char_index[ch] + 1

            char_index[ch] = right
            best = max(best, right - left + 1)

        return best
