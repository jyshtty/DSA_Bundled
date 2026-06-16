"""
Problem: Find Median from Data Stream
Link: https://leetcode.com/problems/find-median-from-data-stream/

Description:
    Design a data structure that supports:
    - addNum(num): add a number to the data structure.
    - findMedian(): return the median of all numbers added so far.

Examples:
    addNum(1), addNum(2), findMedian() -> 1.5
    addNum(3), findMedian() -> 2.0

Constraints:
    -10^5 <= num <= 10^5
    At most 5 * 10^4 calls to addNum and findMedian.
"""

import heapq


class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap for the lower half (negated values)
        self.large = []  # min-heap for the upper half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # ensure every element in small is <= every element in large
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # balance sizes: small can have at most one extra element
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
