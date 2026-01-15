# leetcode 3: Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Approach: Sliding window optimized
# Time Complexity: O(n)
# Space Complexity: O(min(n, 26))
# Implementation:


def foo(s):
    l = 0
    r = 0
    maxi = 0
    dict01 = {}
    while r < len(s):
        if s[r] in dict01:
            if l <= dict01[s[r]]:
                l = dict01[s[r]] + 1
        dict01[s[r]] = r
        maxi = max((r - l + 1), maxi)
        r = r + 1
    return maxi
s = "tmmzuxt"
a = "0123456789"
print(foo(s))




