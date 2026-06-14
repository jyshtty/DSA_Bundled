"""
Problem: Meeting Rooms II
Link: https://leetcode.com/problems/meeting-rooms-ii/

Description:
    Given an array of meeting time intervals, return the minimum number of
    conference rooms required.

Examples:
    Input:  intervals = [[0,30],[5,10],[15,20]]  Output: 2
    Input:  intervals = [[7,10],[2,4]]           Output: 1

Constraints:
    1 <= intervals.length <= 10^4
    0 <= start_i < end_i <= 10^6
"""

import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        # min-heap of end times — tracks when each room becomes free
        heap = []

        for start, end in intervals:
            if heap and heap[0] <= start:
                # reuse the room that ends earliest (it's already free)
                heapq.heapreplace(heap, end)
            else:
                heapq.heappush(heap, end)

        return len(heap)
