"""
Problem: Network Delay Time
Link: https://leetcode.com/problems/network-delay-time/

Description:
    Given n nodes, a list of weighted directed edges, and a source k,
    return the minimum time for all nodes to receive the signal, or -1
    if unreachable.

Examples:
    Input:  times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2    Output: 2

Constraints:
    1 <= k <= n <= 100
    1 <= times.length <= 6000
    0 <= w <= 100
"""

from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Dijkstra: greedily process the nearest unvisited node
        dist = {k: 0}
        heap = [(0, k)]

        while heap:
            d, node = heapq.heappop(heap)
            if d > dist.get(node, float('inf')):
                continue  # stale entry — a shorter path was already found
            for nei, weight in graph[node]:
                new_dist = d + weight
                if new_dist < dist.get(nei, float('inf')):
                    dist[nei] = new_dist
                    heapq.heappush(heap, (new_dist, nei))

        return max(dist.values()) if len(dist) == n else -1
