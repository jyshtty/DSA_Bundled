# leetcode 25: Reverse Nodes in k-Group
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Approach: Reverse in groups
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:




class Solution:
    def reverseKGroup(self, head, k):

        def reverse(head):
            prev = None
            curr = tail_node = head

            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            head = prev
            return head, tail_node

        dummy_node = ListNode()
        curr = dummy_node

        temp = head
        while temp:
            count = 1
            head_to_pass = temp
            while count != k:
                if temp.next:
                    temp = temp.next
                    count += 1
                else:
                    return dummy_node.next
            next = temp.next
            temp.next = None
            h1, t1 = reverse(head_to_pass)

            curr.next = h1
            t1.next = next

            temp = next
            curr = t1

        return dummy_node.next