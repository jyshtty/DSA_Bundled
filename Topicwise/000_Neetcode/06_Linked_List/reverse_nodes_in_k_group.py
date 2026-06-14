"""
Problem: Reverse Nodes in k-Group
Link: https://leetcode.com/problems/reverse-nodes-in-k-group/

Description:
    Given a linked list, reverse nodes k at a time and return the modified
    list. If the number of nodes is not a multiple of k, leave the remaining
    nodes as-is.

Examples:
    Input:  head = [1,2,3,4,5], k = 2    Output: [2,1,4,3,5]
    Input:  head = [1,2,3,4,5], k = 3    Output: [3,2,1,4,5]

Constraints:
    1 <= k <= n <= 5000
    0 <= Node.val <= 1000
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # check if k nodes remain
            kth = self._get_kth(group_prev, k)
            if not kth:
                break

            group_next = kth.next  # node just after the group

            # reverse k nodes
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # reconnect: group_prev now points to the new head of the reversed group
            tmp = group_prev.next   # original first node (now the tail of the reversed group)
            group_prev.next = kth
            group_prev = tmp        # advance group_prev to the tail for the next iteration

        return dummy.next

    def _get_kth(self, curr: ListNode, k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
