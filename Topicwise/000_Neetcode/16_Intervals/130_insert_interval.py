"""
Problem: Insert Interval
Link: https://leetcode.com/problems/insert-interval/

Description:
    Given a sorted list of non-overlapping intervals and a new interval,
    insert and merge as necessary. Return the resulting intervals.

Examples:
    Input:  intervals = [[1,3],[6,9]], newInterval = [2,5]    Output: [[1,5],[6,9]]
    Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]

Constraints:
    0 <= intervals.length <= 10^4
    intervals[i].length == 2
    intervals is sorted by start time.
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # add all intervals that end before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # merge all overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        # add remaining intervals
        result.extend(intervals[i:])
        return result
