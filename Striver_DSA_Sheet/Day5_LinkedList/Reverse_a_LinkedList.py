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