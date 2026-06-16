"""
Problem: Add Two Numbers
Link: https://leetcode.com/problems/add-two-numbers/

Description:
    Two non-empty linked lists represent non-negative integers stored in
    reverse order. Add the two numbers and return the sum as a linked list
    also in reverse order.

Examples:
    Input:  l1 = [2,4,3], l2 = [5,6,4]    Output: [7,0,8]  (342 + 465 = 807)
    Input:  l1 = [9,9,9,9], l2 = [9,9,9]  Output: [8,9,9,0,1]

Constraints:
    1 <= number of nodes <= 100
    0 <= Node.val <= 9
    No leading zeros except the number 0 itself.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            carry, digit = divmod(val, 10)  # carry for next position, digit for current node
            curr.next = ListNode(digit)
            curr = curr.next

        return dummy.next
