# leetcode 2: Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# https://leetcode.com/problems/add-two-numbers/
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Approach: Traverse both lists, add digits with carry
# Time Complexity: O(max(m,n))
# Space Complexity: O(max(m,n))
# Implementation:


# Add Two Numbers
class Node():
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


def add_two_numbers(l1, l2):
    Dummy_head = Node(0)
    temp = Dummy_head

    carry = 0

    while l1 or l2 or carry != 0:  # even if we reach end of l1 and l2, we need to make sure we are using carry hence carry != 0.
        l1val = l1.val if l1 else 0 # if l1 reaches end, we take l1's value as 0
        l2val = l2.val if l2 else 0

        main_sum = l1val + l2val + carry

        carry = main_sum // 10
        unit_place = main_sum % 10

        new_node = Node(unit_place)

        curr.next = new_node
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return Dummy_head.next




