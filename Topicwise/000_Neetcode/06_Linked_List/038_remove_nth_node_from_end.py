"""
Problem: Remove Nth Node From End of List
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Description:
    Given the head of a linked list, remove the nth node from the end
    and return its head. Do it in one pass.

Examples:
    Input:  head = [1,2,3,4,5], n = 2    Output: [1,2,3,5]
    Input:  head = [1], n = 1            Output: []
    Input:  head = [1,2], n = 1          Output: [1]

Constraints:
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # dummy lets us delete the head node without a special case
        fast = dummy

        # advance fast by n+1 steps so the gap between fast and slow is exactly n
        for _ in range(n + 1):
            fast = fast.next

        slow = dummy
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next  # unlink the target node
        return dummy.next
