# leetcode 56: Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
# https://leetcode.com/problems/merge-intervals/
# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Approach: Sort and merge
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Implementation:


def foo(A):
    A.sort()
    r = 1
    ls = []
    merged_array = A[0]
    while r < len(A):
        if merged_array[1] >= A[r][0]:
            merged_array = (merged_array[0], max(merged_array[1], A[r][1]))
        else:
            ls.append(merged_array)
            merged_array = A[r]
        r = r + 1
    ls.append(merged_array)
    return ls

A = [[1,3],[2,6],[8,10],[15,18]]
print(foo(A))






