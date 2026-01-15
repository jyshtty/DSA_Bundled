# leetcode 3: Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Approach: Sliding window with hash set
# Time Complexity: O(n)
# Space Complexity: O(min(n, 26))
# Implementation:


def foo(s):
    a = set()
    l = 0
    r = 0
    maxi = 0
    while(r<len(s)):
        if s[r] not in a:
            a.add(s[r])
            maxi = max((r-l + 1), maxi)
            r = r + 1
        else:
            a.remove(s[l])
            l = l + 1
    return maxi

s = "abcaabcdba"
print(foo(s))











