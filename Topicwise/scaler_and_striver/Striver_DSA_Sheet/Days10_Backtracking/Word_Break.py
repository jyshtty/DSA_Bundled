# leetcode 139: Word Break
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# https://leetcode.com/problems/word-break/
# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Approach: DP or backtracking with memo
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Implementation:


# Use DP Solution

class Solution:
    def wordBreak(self, s, wordDict):
        def wordBreakRecur(s: str, word_dict, start):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dict and wordBreakRecur(s, word_dict, end):
                    return True
            return False

        return wordBreakRecur(s, set(wordDict), 0)