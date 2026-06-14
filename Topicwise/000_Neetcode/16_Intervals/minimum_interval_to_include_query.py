"""
Problem: Minimum Interval to Include Each Query
Link: https://leetcode.com/problems/minimum-interval-to-include-each-query/

Description:
    Given intervals and queries, for each query find the size (end-start+1)
    of the smallest interval containing the query. Return -1 if none.

Examples:
    Input:  intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
    Output: [3,3,1,4]

Constraints:
    1 <= intervals.length <= 10^5
    1 <= queries.length <= 10^5
    queries[i] >= 1
"""

from typing import List
import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        # sort queries but keep original indices to reconstruct the answer
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        heap = []  # (size, end) — min-heap by interval size
        i = 0
        result = {}

        for idx, q in sorted_queries:
            # add all intervals that start at or before q
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(heap, (end - start + 1, end))
                i += 1

            # remove intervals that end before q (they don't contain q)
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            result[idx] = heap[0][0] if heap else -1

        return [result[i] for i in range(len(queries))]
