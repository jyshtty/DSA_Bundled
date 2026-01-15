# leetcode 19: Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Approach: Two pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        size = 1
        cur = p = head
        while cur.next:
            size += 1
            cur = cur.next
            if size > n + 1:
                p = p.next
        if size == n:
            return head.next
        else:
            p.next = p.next.next
            return head

if __name__ == "__main__":
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)

    one.next = two
    two.next = three
    three.next = four
    four.next = five

    head = one

    obj = Solution()
    print(obj.removeNthFromEnd(head, 2))