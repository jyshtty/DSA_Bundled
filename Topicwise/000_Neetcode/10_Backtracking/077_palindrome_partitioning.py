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

class Solution:
    def isPalin(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

    def partition(self, s):
        ans = []
        curr = []
        def backtracking(i):
            if i == len(s):
                ans.append(curr.copy())
                return
            for j in range(i, len(s)):
                if self.isPalin(i, j, s):
                    curr.append(s[i: j + 1])
                    backtracking(j + 1)
                    curr.pop()
        backtracking(0)
        return ans
