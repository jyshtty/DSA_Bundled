"""
Problem: Reverse Linked List
Link: https://leetcode.com/problems/reverse-linked-list/

Description:
    Given the head of a singly linked list, reverse the list and return
    the new head.

Examples:
    Input:  1 -> 2 -> 3 -> 4 -> 5    Output: 5 -> 4 -> 3 -> 2 -> 1
    Input:  1 -> 2                   Output: 2 -> 1
    Input:  []                       Output: []

Constraints:
    0 <= Number of nodes <= 5000
    -5000 <= Node.val <= 5000
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            next_node = curr.next  # save next before overwriting it
            curr.next = prev       # reverse the pointer
            prev = curr
            curr = next_node

        return prev  # prev is the new head once curr falls off the end
