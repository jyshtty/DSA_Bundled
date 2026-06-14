"""
Problem: Merge Intervals
Link: https://leetcode.com/problems/merge-intervals/

Description:
    Given an array of intervals, merge all overlapping intervals and
    return the non-overlapping intervals.

Examples:
    Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]    Output: [[1,6],[8,10],[15,18]]
    Input:  intervals = [[1,4],[4,5]]                   Output: [[1,5]]

Constraints:
    1 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti <= endi <= 10^4
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)  # extend the last merged interval
            else:
                result.append([start, end])

        return result
