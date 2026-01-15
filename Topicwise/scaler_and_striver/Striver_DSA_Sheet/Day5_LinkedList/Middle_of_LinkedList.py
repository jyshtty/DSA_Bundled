# leetcode 876: Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# https://leetcode.com/problems/middle-of-the-linked-list/
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Approach: Fast and slow pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:


class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow