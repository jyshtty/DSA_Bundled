

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