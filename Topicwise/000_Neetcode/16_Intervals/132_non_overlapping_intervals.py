"""
Problem: Non-overlapping Intervals
Link: https://leetcode.com/problems/non-overlapping-intervals/

Description:
    Given an array of intervals, return the minimum number of intervals
    to remove to make the rest non-overlapping.

Examples:
    Input:  intervals = [[1,2],[2,3],[3,4],[1,3]]    Output: 1
    Input:  intervals = [[1,2],[1,2],[1,2]]          Output: 2
    Input:  intervals = [[1,2],[2,3]]                Output: 0

Constraints:
    1 <= intervals.length <= 10^5
    intervals[i].length == 2
    -5 * 10^4 <= starti < endi <= 5 * 10^4
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # sort by end time: greedy — keep earliest ending
        removed = 0
        prev_end = float('-inf')

        for start, end in intervals:
            if start < prev_end:
                removed += 1  # overlap: remove this interval (it ends later than the one we kept)
            else:
                prev_end = end  # keep this interval

        return removed
