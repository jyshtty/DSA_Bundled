"""
Problem: Meeting Rooms
Link: https://leetcode.com/problems/meeting-rooms/

Description:
    Given an array of meeting time intervals [start, end], determine if a
    person can attend all meetings (no two intervals overlap).

Examples:
    Input:  intervals = [[0,30],[5,10],[15,20]]  Output: False
    Input:  intervals = [[7,10],[2,4]]           Output: True

Constraints:
    0 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= start_i < end_i <= 10^6
"""

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            # overlap if previous meeting ends after current one starts
            if intervals[i-1][1] > intervals[i][0]:
                return False

        return True
