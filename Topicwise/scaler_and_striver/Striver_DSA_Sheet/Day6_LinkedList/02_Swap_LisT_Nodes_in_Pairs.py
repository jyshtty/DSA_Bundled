# leetcode 24: Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
# https://leetcode.com/problems/swap-nodes-in-pairs/
# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Approach: Iterative swap
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverse(self, next_1, next_2):
        next_1.next = next_2.next
        next_2.next = next_1
        return next_2

    def swapPairs(self, A):
        start = ListNode(0)
        start.next = A
        curr = start
        while curr.next and curr.next.next:
            curr.next = self.reverse(curr.next, curr.next.next)
            curr = curr.next.next
        return start.next