"""
Problem: Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/

Description:
    Given two strings s and t, return true if t is an anagram of s,
    and false otherwise. An anagram uses the same characters the same
    number of times, in any order.

Examples:
    Input:  s = "anagram", t = "nagaram"    Output: True
    Input:  s = "rat",     t = "car"        Output: False

Constraints:
    1 <= s.length, t.length <= 5 * 10^4
    s and t consist of lowercase English letters
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1  # decrement so overuse of a char is caught (e.g. "aa" vs "ab")

        return True
