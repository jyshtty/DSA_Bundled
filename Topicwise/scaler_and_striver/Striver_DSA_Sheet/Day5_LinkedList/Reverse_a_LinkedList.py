# leetcode 206: Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# https://leetcode.com/problems/reverse-linked-list/
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Approach: Iterative reversal
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        return prev # in line 15 of last iteration you did prev = curr. so when your curr is None, you prev will point to last number.