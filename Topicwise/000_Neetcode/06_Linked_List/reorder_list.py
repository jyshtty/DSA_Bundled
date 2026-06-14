"""
Problem: Reorder List
Link: https://leetcode.com/problems/reorder-list/

Description:
    Given a linked list L0 -> L1 -> ... -> Ln, reorder it to:
    L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
    Do it in-place without altering node values.

Examples:
    Input:  1 -> 2 -> 3 -> 4          Output: 1 -> 4 -> 2 -> 3
    Input:  1 -> 2 -> 3 -> 4 -> 5     Output: 1 -> 5 -> 2 -> 4 -> 3

Constraints:
    1 <= number of nodes <= 5 * 10^4
    1 <= Node.val <= 1000
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # step 1: find the middle using slow/fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: reverse the second half in-place
        prev, curr = None, slow.next
        slow.next = None  # cut the list in half
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # step 3: merge first half and reversed second half alternately
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
