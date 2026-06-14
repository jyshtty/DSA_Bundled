"""
Problem: Merge K Sorted Lists
Link: https://leetcode.com/problems/merge-k-sorted-lists/

Description:
    Given an array of k linked-lists, each sorted in ascending order,
    merge all the linked-lists into one sorted linked-list and return it.

Examples:
    Input:  lists = [[1,4,5],[1,3,4],[2,6]]    Output: [1,1,2,3,4,4,5,6]
    Input:  lists = []                          Output: []

Constraints:
    0 <= k <= 10^4
    0 <= lists[i].length <= 500
    -10^4 <= lists[i][j] <= 10^4
"""

from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # seed heap with the head of each non-empty list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))  # i breaks ties when vals are equal

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
