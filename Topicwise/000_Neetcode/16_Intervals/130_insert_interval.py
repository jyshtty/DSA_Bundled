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
        ans = []
        for int_index in range(len(intervals)):
            if newInterval[1] < intervals[int_index][0]:
                ans.append(newInterval)
                return ans + intervals[int_index:]
            elif intervals[int_index][1] < newInterval[0]:
                ans.append(intervals[int_index])
            else:
                newInterval = [min(newInterval[0], intervals[int_index][0]), max(newInterval[1], intervals[int_index][1])]
        ans.append(newInterval)
        return ans