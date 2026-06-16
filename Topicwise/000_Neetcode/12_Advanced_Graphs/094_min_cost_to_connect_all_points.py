"""
Problem: Min Cost to Connect All Points
Link: https://leetcode.com/problems/min-cost-to-connect-all-points/

Description:
    Given an array of points, return the minimum cost to connect all points
    where cost is the Manhattan distance. (This is Minimum Spanning Tree.)

Examples:
    Input:  points = [[0,0],[2,2],[3,10],[5,2],[7,0]]    Output: 20
    Input:  points = [[3,12],[-2,5],[-4,1]]             Output: 18

Constraints:
    1 <= points.length <= 1000
    -10^6 <= xi, yi <= 10^6
    All points are distinct.
"""

from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        # Prim's algorithm: start from point 0, always pick the cheapest edge to an unvisited node
        heap = [(0, 0)]  # (cost, point_index)
        total = 0

        while len(visited) < n:
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue
            visited.add(i)
            total += cost
            for j in range(n):
                if j not in visited:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(heap, (dist, j))

        return total
