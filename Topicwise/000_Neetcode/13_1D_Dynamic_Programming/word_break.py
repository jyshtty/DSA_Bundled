"""
Problem: Word Break
Link: https://leetcode.com/problems/word-break/

Description:
    Given a string s and a dictionary wordDict, return true if s can be
    segmented into space-separated words all in the dictionary.

Examples:
    Input:  s = "leetcode", wordDict = ["leet","code"]     Output: True
    Input:  s = "applepenapple", wordDict = ["apple","pen"] Output: True
    Input:  s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] Output: False

Constraints:
    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True  # empty string is always valid

        for i in range(1, len(s) + 1):
            for j in range(i):
                # if dp[j] is reachable and s[j:i] is a valid word, dp[i] is reachable
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[len(s)]
