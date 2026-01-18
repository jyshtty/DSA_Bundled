# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# s2 is bigger than s1
# https://leetcode.com/problems/permutation-in-string/

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").      

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# Approach: Sliding Window with Frequency Count
# 1. Create frequency counts for characters in s1 and the first window of s2
# 2. Slide the window over s2, updating the frequency counts
# 3. At each step, compare the frequency counts of the current window with that of s1
# 4. If they match, return True

# Time Complexity: O(n)
# Space Complexity: O(1) - since the character set is fixed (lowercase English letters)

# Implementation:


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts1 = [0] * 26
        counts2 = [0] * 26

        # initialize counts
        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord('a')] += 1 # count for s1
            counts2[ord(s2[i]) - ord('a')] += 1 # count for first window in s2

        # sliding window
        for i in range(len(s2) - len(s1)): # slide the window over s2 if len of s2 is 6 and len of s1 is 2, then slide 4 times.
            if counts1 == counts2:
                return True
            # slide the window: remove left char, add right char
            counts2[ord(s2[i]) - ord('a')] -= 1 # remove left char 
            counts2[ord(s2[i + len(s1)]) - ord('a')] += 1 # add right char

        return counts1 == counts2
