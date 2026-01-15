# leetcode 658: Find K Closest Elements
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
# An integer a is closer to x than an integer b if |a - x| < |b - x|, or |a - x| == |b - x| and a < b.
# https://leetcode.com/problems/find-k-closest-elements/
# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]

# Approach: Heap
# Use a max heap to store the elements with their distances.
# For each element, push [distance, value] into the heap.
# If heap size > k, pop the largest distance.
# Finally, extract the elements and sort.
# Time Complexity: O(n log k)
# Space Complexity: O(k)

# Implementation:

# Find the k closest elements to X
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        from heapq import heapify, heappush, heappop
        
        heap = []
        heapify(heap)
        
        for i in arr:
            diff = abs(x-i)
            heappush(heap, [diff, i])
        
        ans = []
        for i in range(k):
            diff, n = heappop(heap)
            ans.append(n)
        
        return sorted(ans)
