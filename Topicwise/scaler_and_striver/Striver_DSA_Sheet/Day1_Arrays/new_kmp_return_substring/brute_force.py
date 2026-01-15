# Implement strStr()
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# https://leetcode.com/problems/implement-strstr/
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Approach: Brute force
# Time Complexity: O((n-m+1)*m)
# Space Complexity: O(1)
# Implementation:


def kmp_substring_match(A, search):
    for i in range(len(A)-len(search)+1):
        l = 0
        r = i
        while (l < len(search)):
            if A[r] != search[l]:
                break
            else:
                r += 1
                l += 1
        else:
            return "found"
    return "not found"

A = "abcbcglx"
search = "bcglx"
print(kmp_substring_match(A,search))