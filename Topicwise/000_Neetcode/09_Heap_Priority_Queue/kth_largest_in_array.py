"""
Problem: Kth Largest Element in an Array
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

Description:
    Given an integer array nums and an integer k, return the kth largest
    element in the array (not the kth distinct element).

Examples:
    Input:  nums = [3,2,1,5,6,4], k = 2    Output: 5
    Input:  nums = [3,2,3,1,2,4,5,5,6], k = 4    Output: 4

Constraints:
    1 <= k <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
"""

from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maintain a min-heap of size k; root is the kth largest
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)  # heapreplace is faster than pop+push

        return heap[0]
