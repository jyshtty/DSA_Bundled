"""
Problem: Last Stone Weight
Link: https://leetcode.com/problems/last-stone-weight/

Description:
    Each turn, smash the two heaviest stones. If equal, both are destroyed.
    If different, the lighter one is destroyed and the heavier one remains
    with weight (heavy - light). Return the last stone's weight, or 0.

Examples:
    Input:  stones = [2,7,4,1,8,1]    Output: 1
    Input:  stones = [1]              Output: 1

Constraints:
    1 <= stones.length <= 30
    1 <= stones[i] <= 1000
"""

from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # negate values to simulate a max-heap using Python's min-heap
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            heavy = -heapq.heappop(heap)
            light = -heapq.heappop(heap)
            if heavy != light:
                heapq.heappush(heap, -(heavy - light))

        return -heap[0] if heap else 0
