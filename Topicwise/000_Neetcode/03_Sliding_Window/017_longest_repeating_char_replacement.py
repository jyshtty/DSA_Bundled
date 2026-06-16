"""
Problem: Longest Repeating Character Replacement
Link: https://leetcode.com/problems/longest-repeating-character-replacement/

Description:
    Given a string s and integer k, you can replace at most k characters.
    Return the length of the longest substring containing the same letter
    after performing at most k replacements.

Examples:
    Input:  s = "ABAB", k = 2    Output: 4
    Input:  s = "AABABBA", k = 1 Output: 4

Constraints:
    1 <= s.length <= 10^5
    s consists of only uppercase English letters.
    0 <= k <= s.length
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0  # tracks the highest frequency of any single char in the window
        best = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # window size minus the dominant char count = chars we need to replace
            # if that exceeds k, the window is invalid — shrink from the left
            window_size = right - left + 1
            if window_size - max_freq > k:
                count[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
