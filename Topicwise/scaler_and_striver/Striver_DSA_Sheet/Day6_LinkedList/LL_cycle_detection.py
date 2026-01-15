# leetcode 141: Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# https://leetcode.com/problems/linked-list-cycle/
# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Approach: Fast and slow pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:


#Approach 1
class Solution:
    def hasCycle(self, head):
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False

#APPROACH 2

class Solution:
    def hasCycle(self, head):
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
