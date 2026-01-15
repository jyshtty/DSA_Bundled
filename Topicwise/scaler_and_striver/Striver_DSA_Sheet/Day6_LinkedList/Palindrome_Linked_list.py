# leetcode 234: Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome.
# https://leetcode.com/problems/palindrome-linked-list/
# Example 1:
# Input: head = [1,2,2,1]
# Output: true
# Approach: Find middle, reverse second half, compare
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return
        if not head.next:
            return True

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if fast:
            slow = slow.next

        def reverse(head):

            curr = head
            prev = None

            while curr:
                next = curr.next
                curr.next = prev

                prev = curr
                curr = next

            return prev

        rev_head = reverse(slow)

        temp1 = head
        temp2 = rev_head

        while temp2:
            if temp1.val != temp2.val:
                return False
            temp1 = temp1.next
            temp2 = temp2.next

        return True


one = ListNode(1)
two = ListNode(2)
three = ListNode(2)
four = ListNode(1)
# five = ListNode(5)

one.next = two
two.next = three
three.next = four
# four.next = five

head = one
obj = Solution()
print(obj.isPalindrome(head))