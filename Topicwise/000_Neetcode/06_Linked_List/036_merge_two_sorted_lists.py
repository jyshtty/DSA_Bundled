"""
Problem: Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/

Description:
    Merge two sorted linked lists and return the head of the merged list.
    The merged list should be sorted.

Examples:
    Input:  l1 = 1->2->4, l2 = 1->3->4    Output: 1->1->2->3->4->4
    Input:  l1 = [], l2 = []               Output: []
    Input:  l1 = [], l2 = [0]              Output: [0]

Constraints:
    0 <= number of nodes in each list <= 50
    -100 <= Node.val <= 100
    Both lists are sorted in non-decreasing order.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # sentinel node so we never have to handle an empty result list
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2  # attach the remaining non-empty list
        return dummy.next
