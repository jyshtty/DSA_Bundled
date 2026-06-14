"""
Problem: K Closest Points to Origin
Link: https://leetcode.com/problems/k-closest-points-to-origin/

Description:
    Given an array of points on a plane, return the k closest points to
    the origin (0, 0). Distance is Euclidean. Order of answer doesn't matter.

Examples:
    Input:  points = [[1,3],[-2,2]], k = 1    Output: [[-2,2]]
    Input:  points = [[3,3],[5,-1],[-2,4]], k = 2    Output: [[3,3],[-2,4]]

Constraints:
    1 <= k <= points.length <= 10^4
    -10^4 <= xi, yi <= 10^4
"""

from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max-heap of size k: keep the k closest by evicting the farthest
        heap = []
        for x, y in points:
            dist = -(x * x + y * y)  # negate for max-heap; skip sqrt (monotone transformation)
            heapq.heappush(heap, (dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for _, x, y in heap]
