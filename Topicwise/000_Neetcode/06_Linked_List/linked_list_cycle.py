"""
Problem: Linked List Cycle
Link: https://leetcode.com/problems/linked-list-cycle/

Description:
    Given the head of a linked list, determine if the list has a cycle.

Examples:
    Input:  head = [3,2,0,-4], pos = 1    Output: True  (tail connects to index 1)
    Input:  head = [1,2], pos = 0         Output: True
    Input:  head = [1], pos = -1          Output: False

Constraints:
    0 <= number of nodes <= 10^4
    -10^5 <= Node.val <= 10^5
    pos is -1 or a valid index.
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:  # Floyd's cycle detection: they meet only inside a cycle
                return True

        return False
