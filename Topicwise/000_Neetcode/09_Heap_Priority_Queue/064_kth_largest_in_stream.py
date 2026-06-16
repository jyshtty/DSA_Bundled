"""
Problem: Kth Largest Element in a Stream
Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/

Description:
    Design a class to find the kth largest element in a stream.
    add(val) adds val to the stream and returns the kth largest element.

Examples:
    KthLargest(3, [4,5,8,2])
    add(3)  -> 4
    add(5)  -> 5
    add(10) -> 5
    add(9)  -> 8
    add(4)  -> 8

Constraints:
    1 <= k <= 10^4
    0 <= nums.length <= 10^4
    -10^4 <= nums[i], val <= 10^4
    At most 10^4 calls to add.
"""

from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []  # min-heap of size k; the root is always the kth largest
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)  # evict the smallest to maintain exactly k elements
        return self.heap[0]
